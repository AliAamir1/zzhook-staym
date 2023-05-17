import { Given, When, Then } from "cucumber";
import { expect } from "chai";
import mongoose from "mongoose";
import SurahModel, { Surah } from "../../src/models/surah.model";

Given("the database is empty", async () => {
  await SurahModel.deleteMany({});
});

Given(
  "the following surahs exist in the database:",
  async (surahs: Surah[]) => {
    await SurahModel.insertMany(surahs);
  }
);

When("I get the surah with number {int}", async (number: number) => {
  this.result = await SurahModel.getSurahByNumber(number);
});

When("I get the surah with name {string}", async (name: string) => {
  this.result = await SurahModel.getSurahByName(name);
});

When("I get all surahs", async () => {
  this.result = await SurahModel.getSurahs();
});

When("I create a new surah with the following details:", async (table) => {
  const newSurah: Surah = table.rowsHash() as Surah;
  this.result = await SurahModel.createSurah(newSurah);
});

When("I update the surah with the following details:", async (table) => {
  const updatedSurah: Surah = table.rowsHash() as Surah;
  this.result = await SurahModel.updateSurah(updatedSurah);
});

When("I delete the surah with number {int}", async (number: number) => {
  this.result = await SurahModel.deleteSurah(number);
});

Then("the result should be a surah with number {int}", async (number: number) => {
  expect(this.result).to.exist;
  expect(this.result.number).to.equal(number);
});

Then("the result should be a surah with name {string}", async (name: string) => {
  expect(this.result).to.exist;
  expect(this.result.name).to.equal(name);
});

Then("the result should be an array of surahs", async () => {
  expect(this.result).to.exist;
  expect(this.result).to.be.an("array");
});

Then("the array should contain {int} surahs", async (count: number) => {
  expect(this.result).to.have.lengthOf(count);
});

Then(
  "the surah with number {int} should have name {string}",
  async (number: number, name: string) => {
    const surah = this.result.find((s: Surah) => s.number === number);
    expect(surah).to.exist;
    expect(surah.name).to.equal(name);
  }
);

Then(
  "the surah with number {int} should not exist",
  async (number: number) => {
    const surah = await SurahModel.getSurahByNumber(number);
    expect(surah).to.not.exist;
  }
);

Then("the result should be a modified count of {int}", async (count: number) => {
  expect(this.result.nModified).to.equal(count);
});

Then("the result should be a deleted count of {int}", async (count: number) => {
  expect(this.result.deletedCount).to.equal(count);
});
