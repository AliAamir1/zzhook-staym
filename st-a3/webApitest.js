import axios from "axios";

describe("Quran.com API Tests", () => {
  const api = axios.create({
    baseURL: "https://api.quran.com/api/v4",
  });

  let token;

  beforeAll(async () => {
    const response = await api.post("/auth/login", {
      email: "testuser@example.com",
      password: "testpassword",
    });
    token = response.data.token;
  });

  describe("Scenario 1: Get All Surahs", () => {
    test("should return status code 200", async () => {
      const response = await api.get("/chapters");
      expect(response.status).toBe(200);
    });

    test("should return an array of 114 surahs", async () => {
      const response = await api.get("/chapters");
      expect(response.data.chapters.length).toBe(114);
    });
  });

  describe("Scenario 2: Retrieve Contents of a Single Surah", () => {
    let surahId;

    beforeAll(async () => {
      const response = await api.get("/chapters");
      surahId = response.data.chapters[0].id; // assume the first surah
    });

    test("should return status code 200", async () => {
      const response = await api.get(`/chapters/${surahId}`);
      expect(response.status).toBe(200);
    });

    test("should return the correct surah details", async () => {
      const response = await api.get(`/chapters/${surahId}`);
      const surah = response.data.chapter;
      expect(surah.id).toBe(surahId);
      expect(surah.bismillah_pre).toBe(1);
      expect(surah.verses_count).toBeGreaterThan(0);
    });
  });

  describe("Scenario 3: Successfully Login", () => {
    test("should return status code 200 and a valid token", async () => {
      const response = await api.post("/auth/login", {
        email: "testuser@example.com",
        password: "testpassword",
      });
      expect(response.status).toBe(200);
      expect(response.data.token).toBeTruthy();
    });

    test("should return status code 401 with invalid credentials", async () => {
      const response = await api
        .post("/auth/login", {
          email: "invalid@example.com",
          password: "invalidpassword",
        })
        .catch((error) => error.response);
      expect(response.status).toBe(401);
    });
  });
});
