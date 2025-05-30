const express = require('express');
const bodyParser = require('body-parser');
const { MongoClient } = require('mongodb');

const app = express();
const port = 3000;
const mongoURL = "mongodb://localhost:27017";

app.use(bodyParser.urlencoded({ extended: true }));

app.post('/register', async (req, res) => {
  const { name, email } = req.body;

  try {
    const client = new MongoClient(mongoURL);
    await client.connect();
    const db = client.db("registration");
    const users = db.collection("users");
    await users.insertOne({ name, email });
    client.close();

    res.send("Registered successfully!");
  } catch (err) {
    res.status(500).send("Error registering user");
  }
});

app.listen(port, () => {
  console.log(`App running on http://localhost:${port}`);
});
