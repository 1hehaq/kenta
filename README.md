# Kenta - Subdomain Enumeration Tool

Discover subdomains effortlessly with Kenta! This Python tool integrates popular subdomain discovery tools like Amass, Subfinder, Findomain, Assetfinder, and CRT.sh. Easily enumerate subdomains for a specified domain, with options for recursive enumeration and utilizing all available sources.

### Features

- **Multi-Source Enumeration**: Kenta leverages various subdomain enumeration tools, including Amass, Subfinder, Findomain, Assetfinder, and CRT.sh, to ensure comprehensive coverage.

- **Customizable Enumeration**: Users can customize the enumeration process by enabling recursive scanning and selecting specific sources for enumeration.

- **Efficient Output Handling**: Kenta aggregates subdomain results from different tools into a single output file, simplifying analysis and reporting.

- **Version Information**: Kenta provides users with the ability to check the tool's version, ensuring compatibility and feature awareness.

- **User-Friendly Interface**: The tool offers a command-line interface with options for verbose output, color customization, and silent mode for streamlined operation.

### Merits

- **Comprehensive Coverage**: By integrating multiple subdomain enumeration tools, Kenta ensures thorough reconnaissance, increasing the likelihood of discovering relevant subdomains.

- **Customizable Options**: Users have the flexibility to tailor the enumeration process according to their requirements, enabling efficient scanning based on specific parameters.

- **Unified Output**: Kenta consolidates subdomain results from different sources into a single output file, facilitating easy analysis and reporting for security assessments.

### Demerits

- **Dependency Management**: Kenta relies on external dependencies such as Amass, Subfinder, Findomain, Assetfinder, and jq, which need to be installed separately. Ensuring compatibility and managing dependencies across different environments may pose challenges.

- **Execution Time**: Enabling all available sources for enumeration (using the `-all` option) may significantly increase execution time, especially for large domains, potentially impacting operational efficiency.

### Usage

1. **Installation**:

   - Clone the repository:
     ```
     git clone https://github.com/1hehaq/Kenta.git
     ```

2. **Dependencies**:

   - Ensure that the necessary dependencies are installed. These typically include Python 3.x, Amass, Subfinder, Findomain, Assetfinder, and jq (for CRT.sh).

3. **Usage**:

   - Run Kenta from the command line, specifying the target domain(s) and desired options:
     ```
     python kenta.py -d example.com -o output.txt
     ```

4. **Options**:

   - `-d, --domain`: Specify the target domain(s) for subdomain enumeration.
   - `-o, --output`: Specify the output file to store the enumerated subdomains.
   - `-recursive`: Enable recursive scanning for subdomains.
   - `-all`: Use all available sources for enumeration (may increase execution time).
   - `-silent`: Show only subdomains in the output.
   - `-version`: Display the version of Kenta.
   - `-v, --verbose`: Enable verbose output.
   - `-nc, --no-color`: Disable color in the output.
   - `-ls, --list-sources`: List all available sources for enumeration.

### Acknowledgments

Kenta utilizes open-source subdomain enumeration tools and libraries, including Amass, Subfinder, Findomain, Assetfinder, and jq. Special thanks to the developers and contributors of these projects for their valuable contributions to the cybersecurity community.

---
