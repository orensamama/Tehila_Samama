$root = Split-Path $MyInvocation.MyCommand.Path
$listener = [System.Net.HttpListener]::new()
$listener.Prefixes.Add('http://localhost:3333/')
$listener.Start()
Write-Host "Server running on http://localhost:3333/"
while ($listener.IsListening) {
    $ctx = $listener.GetContext()
    $path = $ctx.Request.Url.LocalPath
    if ($path -eq '/' -or $path -eq '/index.html') { $file = 'index.html' }
    else { $file = $path.TrimStart('/') }
    $full = Join-Path $root $file
    if (Test-Path $full) {
        $bytes = [IO.File]::ReadAllBytes($full)
        $ctx.Response.ContentType = 'text/html; charset=utf-8'
        $ctx.Response.ContentLength64 = $bytes.Length
        $ctx.Response.OutputStream.Write($bytes, 0, $bytes.Length)
    } else {
        $ctx.Response.StatusCode = 404
    }
    $ctx.Response.Close()
}
