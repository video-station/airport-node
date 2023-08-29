const express = require("express");
const exceljs = require("exceljs");
const bodyParser = require("body-parser");
const path = require("path");

const app = express();
const port = 3001;

app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));

const entries = []; // Array to store user-entered data

// Read initial entries from the Excel file
const excelFilePath = path.join(__dirname, "data", "airport.xlsx");
const workbook = new exceljs.Workbook();

workbook.xlsx
  .readFile(excelFilePath)
  .then(() => {
    const worksheet = workbook.worksheets[0];
    worksheet.eachRow((row, rowNumber) => {
      if (rowNumber !== 1) {
        // Skip the header row
        const [airlineCode, airlineName, zone, gate] = row.values;
        entries.push({ airlineCode, airlineName, zone, gate });
      }
    });
  })
  .catch((error) => {
    console.error("Error reading Excel file:", error);
  });

function updateExcelFile() {
  const worksheet = workbook.getWorksheet();
  worksheet.spliceRows(2, worksheet.rowCount - 1); // Remove existing data rows (except header)

  for (const entry of entries) {
    worksheet.addRow([
      entry.airlineCode,
      entry.airlineName,
      entry.zone,
      entry.gate,
    ]);
  }

  return workbook.xlsx
    .writeFile(excelFilePath)
    .then(() => {
      console.log("Excel file updated.");
    })
    .catch((error) => {
      console.error("Error updating Excel file:", error);
    });
}
// Route for the index page
app.get("/", (req, res) => {
  res.render("upload", { entries });
});

// Route to handle form submission
app.post("/", (req, res) => {
  const { airlineCode, airlineName, zone, gate } = req.body;
  entries.push({ airlineCode, airlineName, zone, gate });

  updateExcelFile();

  res.redirect("/");
});

app.post("/delete/:index", (req, res) => {
  const index = parseInt(req.params.index);
  if (index >= 0 && index < entries.length) {
    entries.splice(index, 1);
    console.log(entries)
    updateExcelFile().then(() => {
      res.redirect("/");
    });
  } else {
    res.redirect("/");
  }
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});
