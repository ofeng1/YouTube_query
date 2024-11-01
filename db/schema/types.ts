import { customType } from "drizzle-orm/pg-core";

export const pgVector = (name: string, vectorLength: number) =>
  customType<{ data: number[]; driverData: string }>({
    dataType() {
      return `vector(${vectorLength})`;
    },
    toDriver(value: number[]): string {
      return JSON.stringify(value);
    },
    fromDriver(value: string): number[] {
      return JSON.parse(value as string);
    },
  })(name);

export const tsVector = customType<{ data: string[]; driverData: string }>({
  dataType() {
    return `tsvector`;
  },
});
