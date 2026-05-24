from datetime import datetime


def generate_report(target,
                    ports,
                    banners,
                    header_results,
                    ssl_result,
                    vulnerabilities):

    filename = f"output/report_{target}.html"

    html = f"""
    <html>
    <head>
        <title>SecureScan Report</title>

        <style>
            body {{
                font-family: Arial;
                background: #111;
                color: #0f0;
                padding: 20px;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}

            th, td {{
                border: 1px solid #0f0;
                padding: 10px;
                text-align: left;
            }}

            h1, h2 {{
                color: cyan;
            }}
        </style>
    </head>

    <body>

    <h1>SecureScan Vulnerability Report</h1>

    <p><b>Target:</b> {target}</p>
    <p><b>Generated:</b> {datetime.now()}</p>

    <h2>Open Ports</h2>

    <table>
        <tr>
            <th>Port</th>
            <th>Service</th>
            <th>Banner</th>
            <th>Vulnerability</th>
        </tr>
    """

    for port, service in ports:

        banner = banners.get(port, "N/A")
        vuln = vulnerabilities.get(port, "N/A")

        html += f"""
        <tr>
            <td>{port}</td>
            <td>{service}</td>
            <td>{banner}</td>
            <td>{vuln}</td>
        </tr>
        """

    html += "</table>"

    html += "<h2>HTTP Security Headers</h2>"

    for header, status in header_results.items():
        html += f"<p>{header}: {status}</p>"

    html += "<h2>SSL Information</h2>"

    for key, value in ssl_result.items():
        html += f"<p>{key}: {value}</p>"

    html += """
    </body>
    </html>
    """

    with open(filename, "w") as file:
        file.write(html)

    return filename