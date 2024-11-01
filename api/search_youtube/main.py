import ssl

from pypika import Parameter, Query, Table

from search_youtube.execute_sql import execute, execute_and_fetch_all
from search_youtube.transcription import convert_audio_to_text
from search_youtube.utils import split_text

from .embeddings import get_embeddings
from .execute_sql import execute, execute_and_fetch_all
from .video import download_youtube_video

ssl._create_default_https_context = ssl._create_stdlib_context

sentence_table = Table("sentences")
video_table = Table("videos")
sentence_embeddings_table = Table("sentence_embeddings")


def insert_video_query():
    return (
        Query.into(video_table)
        .columns(video_table.link)
        .insert(Parameter("%s"))
        .returning(video_table.id)
    )


def insert_sentence_blocks_query(num_sentences: int):
    return (
        Query.into(sentence_table)
        .columns(
            sentence_table.content,
            sentence_table.video_id,
        )
        .insert(*[[Parameter("%s")] * 2 for _ in range(num_sentences)])
    )


def get_sentence_blocks_query():
    return (
        Query.from_(sentence_table)
        .select(
            sentence_table.id,
            sentence_table.content,
        )
        .where(sentence_table.video_id == Parameter("%s"))
    )


def insert_embeddings_query(num_embeddings: int):
    return (
        Query.into(sentence_embeddings_table)
        .columns(
            sentence_embeddings_table.embedding,
            sentence_embeddings_table.sentence_id,
            sentence_embeddings_table.video_id,
        )
        .insert(*[[Parameter("%s")] * 3 for _ in range(num_embeddings)])
    )


user_link = input("Give me your link 😩: ")
downloaded_file_path = download_youtube_video(user_link, as_local_file=True)

insert_video_result = execute_and_fetch_all(insert_video_query(), (user_link,))
video_id = insert_video_result[0][0]

transcript = convert_audio_to_text(downloaded_file_path)
sentences = split_text(transcript, 1)

sentence_args = []
for sentence in sentences:
    sentence_args += [
        sentence,
        video_id,
    ]

execute(insert_sentence_blocks_query(len(sentences)), sentence_args)

sentence_blocks = execute_and_fetch_all(get_sentence_blocks_query(), (video_id,))
contents = [block[1] for block in sentence_blocks]
embeddings = get_embeddings(contents)

embedding_args = []
for i in range(len(sentence_blocks)):
    embedding_args += [
        f"[{','.join([str(x) for x in embeddings[i]])}]",
        sentence_blocks[i][0],
        video_id,
    ]

execute(insert_embeddings_query(len(embeddings)), embedding_args)
