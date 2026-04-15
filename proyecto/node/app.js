const express = require("express");
const mysql = require("mysql2");

const app = express();
const PORT = 3000;


const connection = mysql.createConnection({
  host: "mysql_db",
  user: "root",
  password: "root",
  database: "parcial_db"
});

connection.connect((err) => {
  if (err) {
    console.error("Error conectando a la DB:", err);
    return;
  }
  console.log("Conectado a MySQL");
});

app.get("/", (req, res) => {
  connection.query("SELECT * FROM usuarios", (err, results) => {
    if (err) return res.send("Error en consulta");
    res.json(results);
  });
});

app.listen(PORT, () => {
  console.log(`Servidor Node corriendo en puerto ${PORT}`);
});