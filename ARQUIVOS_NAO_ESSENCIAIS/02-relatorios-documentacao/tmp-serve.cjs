const http = require('http');
const fs = require('fs');
const path = require('path');

const PORTS = { cliente: 8790, kds: 8791, kiosk: 8792, admin: 8793 };

function serve(dir, port) {
  const server = http.createServer((req, res) => {
    let filePath = path.join(dir, req.url === '/' ? 'index.html' : req.url);
    if (!fs.existsSync(filePath) || fs.statSync(filePath).isDirectory()) {
      filePath = path.join(dir, 'index.html');
    }
    const ext = path.extname(filePath);
    const mime = {
      '.html': 'text/html', '.js': 'application/javascript', '.css': 'text/css',
      '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp',
      '.svg': 'image/svg+xml', '.json': 'application/json', '.woff2': 'font/woff2',
    }[ext] || 'application/octet-stream';

    fs.readFile(filePath, (err, data) => {
      if (err) {
        res.writeHead(404); res.end('Not found');
      } else {
        res.writeHead(200, { 'Content-Type': mime, 'Access-Control-Allow-Origin': '*' });
        res.end(data);
      }
    });
  });
  server.listen(port, () => console.log(`[${dir}] http://localhost:${port}`));
}

serve('dist/cliente', PORTS.cliente);
serve('dist/kds', PORTS.kds);
serve('dist/kiosk', PORTS.kiosk);
serve('dist/admin', PORTS.admin);

// Keepalive para evitar timeout
setInterval(() => console.log('[keepalive]', new Date().toISOString()), 30000);
