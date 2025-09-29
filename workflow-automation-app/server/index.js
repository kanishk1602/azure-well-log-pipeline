// index.js
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.send('Workflow Automation API running');
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
