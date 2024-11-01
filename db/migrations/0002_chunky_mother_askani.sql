CREATE TABLE IF NOT EXISTS "videos" (
	"id" serial PRIMARY KEY NOT NULL,
	"createdAt" timestamp DEFAULT now() NOT NULL,
	"link" text NOT NULL,
	CONSTRAINT "videos_link_unique" UNIQUE("link")
);
--> statement-breakpoint
ALTER TABLE "sentences" RENAME COLUMN "text" TO "content";--> statement-breakpoint
ALTER TABLE "sentence_embeddings" ADD COLUMN "sentence_id" integer NOT NULL;--> statement-breakpoint
ALTER TABLE "sentence_embeddings" ADD COLUMN "video_id" integer NOT NULL;--> statement-breakpoint
ALTER TABLE "sentences" ADD COLUMN "video_id" integer NOT NULL;--> statement-breakpoint
DO $$ BEGIN
 ALTER TABLE "sentence_embeddings" ADD CONSTRAINT "sentence_embeddings_sentence_id_sentences_id_fk" FOREIGN KEY ("sentence_id") REFERENCES "sentences"("id") ON DELETE cascade ON UPDATE cascade;
EXCEPTION
 WHEN duplicate_object THEN null;
END $$;
--> statement-breakpoint
DO $$ BEGIN
 ALTER TABLE "sentence_embeddings" ADD CONSTRAINT "sentence_embeddings_video_id_videos_id_fk" FOREIGN KEY ("video_id") REFERENCES "videos"("id") ON DELETE cascade ON UPDATE cascade;
EXCEPTION
 WHEN duplicate_object THEN null;
END $$;
--> statement-breakpoint
DO $$ BEGIN
 ALTER TABLE "sentences" ADD CONSTRAINT "sentences_video_id_videos_id_fk" FOREIGN KEY ("video_id") REFERENCES "videos"("id") ON DELETE cascade ON UPDATE cascade;
EXCEPTION
 WHEN duplicate_object THEN null;
END $$;
