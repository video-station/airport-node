const express = require('express');
const http = require('http');
const path = require('path');
const chokidar = require('chokidar');
const xlsx = require('xlsx');
const WebSocket = require('ws');

const app = express();
const port = 3000;

const excelFilePath = 'data/airport.xlsx'; // Replace with the actual path
const viewsPath = path.join(__dirname, 'views');

// Set up EJS as the view engine
app.set('view engine', 'ejs');
app.set('views', viewsPath);

// Serve static files from the "public" directory
app.use(express.static('public'));

let sheetData = []; // Store the Excel data

// Read and store the Excel data initially
function readExcelData() {
  const workbook = xlsx.readFile(excelFilePath);
  const sheetName = workbook.SheetNames[0];
  sheetData = xlsx.utils.sheet_to_json(workbook.Sheets[sheetName]);
}

// Watch for changes in the Excel file
chokidar.watch(excelFilePath).on('change', (event, path) => {
  console.log('File changed:', event);
  readExcelData(); // Update the stored Excel data
  broadcastData(sheetData); // Broadcast the updated data to clients
});

// Route to display the HTML page
app.get('/', (req, res) => {
    readExcelData();
  res.render('index', { data: sheetData });
});

// Create an HTTP server
const server = http.createServer(app);

// Create a WebSocket server
const wss = new WebSocket.Server({ server });

// Broadcast data to connected clients
function broadcastData(data) {
  wss.clients.forEach(client => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(JSON.stringify(data));
    }
  });
}

// Start the HTTP server
server.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});