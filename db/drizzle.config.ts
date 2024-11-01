import { defineConfig } from "drizzle-kit";
import dotenv from "dotenv";

dotenv.config();

export default defineConfig({
  schema: "./schema/index.ts",
  driver: "pg",
  dbCredentials: {
    connectionString: process.env.CONNECTION_STRING || "",
  },
  verbose: true,
  strict: true,
  out: "./migrations",
});
