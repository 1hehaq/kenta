# Author: 1hehaq
# Tool: Kenta
# Version: V1.0

import subprocess
import sys
import argparse
import termcolor
import time

def print_banner():
    banner = r"""
                                                      
    _/    _/                        _/                
   _/  _/      _/_/    _/_/_/    _/_/_/_/    _/_/_/   
  _/_/      _/_/_/_/  _/    _/    _/      _/    _/    
 _/  _/    _/        _/    _/    _/      _/    _/     
_/    _/    _/_/_/  _/    _/      _/_/    _/_/_/      
                                                      

                                    @1hehaq🥷                     

    """
    print(termcolor.colored(banner, "cyan"))

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        handle_error(f"Command '{command}' failed with error: {e.stderr}")

def handle_error(msg):
    print(termcolor.colored(f"Error: {msg}", "red"))
    sys.exit(1)

def subdomain_enum(domain, recursive, all_sources, silent):
    start_time = time.time()

    if not silent:
        print(termcolor.colored(f"[INFO] Current Kenta version v1.0 (latest)", "green"))
        print(termcolor.colored(f"[INFO] Kenta started enumeration for {domain}...", "green"))
        def main():
            print_banner()

    # Define commands for various subdomain enumeration tools
    amass_cmd = f"amass enum -d {domain}"
    if recursive:
        amass_cmd += " -recursive"
    if all_sources:
        amass_cmd += " -active"
    amass_cmd += " -o amass.txt"

    subfinder_cmd = f"subfinder -d {domain}"
    if recursive:
        subfinder_cmd += " -recursive"
    if all_sources:
        subfinder_cmd += " -all"
    subfinder_cmd += " -silent -o subfinder.txt"

    findomain_cmd = f"findomain --target {domain} --quiet -u findomain.txt"
    assetfinder_cmd = f"assetfinder --subs-only {domain} > assetfinder.txt"
    crtsh_cmd = f"curl -s 'https://crt.sh/?q=%25.{domain}&output=json' | jq -r '.[].name_value' > crtsh.txt"

    # Run the commands and collect results
    run_command(amass_cmd)
    run_command(subfinder_cmd)
    run_command(findomain_cmd)
    run_command(assetfinder_cmd)
    run_command(crtsh_cmd)

    # Collect results from all tools
    with open("amass.txt") as f1, open("subfinder.txt") as f2, open("findomain.txt") as f3, open("assetfinder.txt") as f4, open("crtsh.txt") as f5:
        subdomains = set(f1.read().splitlines() + f2.read().splitlines() + f3.read().splitlines() + f4.read().splitlines() + f5.read().splitlines())

    end_time = time.time()
    elapsed_time = end_time - start_time
    elapsed_str = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

    if not silent:
        print(termcolor.colored(f"[INFO] Subdomain enumeration completed.", "green"))
        print(termcolor.colored(f"[INFO] Found {len(subdomains)} subdomains for {domain} in {elapsed_str}", "green"))

    return list(subdomains)

def main():
    print_banner()

    parser = argparse.ArgumentParser(description="Subdomain Enumeration Tool")
    parser.add_argument("-d", "--domain", help="Domains to enumerate subdomains for", nargs="+", required=True)
    parser.add_argument("-dL", "--list", help="File containing list of domains for subdomain discovery")
    parser.add_argument("-o", "--output", help="Output file for the subdomains", required=True)
    parser.add_argument("-recursive", action="store_true", help="Use only sources that can handle subdomains recursively")
    parser.add_argument("-all", action="store_true", help="Use all sources for enumeration (slow)")
    parser.add_argument("-silent", action="store_true", help="Show only subdomains in output")
    parser.add_argument("-version", action="store_true", help="Show version of Kenta")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show verbose output")
    parser.add_argument("-nc", "--no-color", action="store_true", help="Disable color in output")
    parser.add_argument("-ls", "--list-sources", action="store_true", help="List all available sources")

    args = parser.parse_args()

    if args.no_color:
        termcolor.TERM_COLOR = None

    if args.version:
        print(termcolor.colored("Kenta version v1.2", "yellow"))
        sys.exit(0)

    if args.list_sources:
        sources = ["amass", "subfinder", "findomain", "assetfinder", "crtsh"]
        print(termcolor.colored("Available sources:", "yellow"))
        for source in sources:
            print(termcolor.colored(f"- {source}", "yellow"))
        sys.exit(0)

    domains = args.domain
    if args.list:
        with open(args.list) as f:
            domains.extend(f.read().splitlines())

    output_file = args.output
    recursive = args.recursive
    all_sources = args.all
    silent = args.silent

    all_subdomains = set()
    for domain in domains:
        subdomains = subdomain_enum(domain, recursive, all_sources, silent)
        all_subdomains.update(subdomains)

    with open(output_file, "w") as f:
        f.write("\n".join(all_subdomains))
    
    if not silent:
        print(termcolor.colored(f"[INFO] Subdomain enumeration results saved to {output_file}", "green"))

if __name__ == "__main__":
    main()
