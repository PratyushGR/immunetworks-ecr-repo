const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());

const port = process.env.PORT || 3002;

app.use(express.json());

app.post('/submit-name', (req, res) => {
    const { name } = req.body;
    console.log(`received name: ${name}`);
    res.send(`Hello ${name}!`);
});

app.listen(port, () => {
    console.log(`Server started at http://localhost:${port}`);
});