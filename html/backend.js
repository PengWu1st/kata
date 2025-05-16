const express = require("express");
const axios = require("axios");
const cors = require("cors"); // 引入 cors 中间件
const app = express();

app.use(cors()); // 启用 cors 中间件
app.use(express.json());

app.post("/verify-recaptcha", async (req, res) => {
  const { token } = req.body;
  console.log("verify-recaptcha");
  try {
    const response = await axios.post(
      `https://www.google.com/recaptcha/api/siteverify?secret=6LdCegArAAAAAGwTdW7PKHKQDBpka1iraRNeargd&response=${token}`
    );

    const { success, score } = response.data;
    res.json({ success, score });
  } catch (error) {
    res.json({ success: false, error: error.message });
  }
});

app.post("/verify-turnstile", async (req, res) => {
  const { token } = req.body;
  console.log("verify-turnstile");

  try {
    const response = await axios.post(
      "https://challenges.cloudflare.com/turnstile/v0/siteverify",
      {
        secret: "0x4AAAAAABCj7bZL3OkWaJm-Wr4WdYAJjNo", // 替换为你的 secret key
        response: token,
      }
    );

    res.json({ success: response.data.success });
  } catch (error) {
    res.json({ success: false, error: error.message });
  }
});

app.listen(9000, () => {
  console.log("Server running on port 9000");
});
