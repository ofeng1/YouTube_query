CREATE TABLE IF NOT EXISTS "sentences" (
	"id" serial PRIMARY KEY NOT NULL,
	"createdAt" timestamp DEFAULT now() NOT NULL,
	"text" text NOT NULL
);
