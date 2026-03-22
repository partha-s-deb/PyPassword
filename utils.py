def print_banner():
    print("""
██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
██╔═══╝   ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
██║        ██║   ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
╚═╝        ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
    """)


def print_separator():
    print("-" * 60)


def print_report(password, strength_result, breach_result):
    print_separator()
    print(f"  Generated Password : {password}")
    print(f"  Entropy            : {strength_result['entropy']} bits")
    print(f"  Strength           : {strength_result['rating']}")

    if strength_result["reasons"]:
        print(f"  Warnings           : {', '.join(strength_result['reasons'])}")

    if breach_result["checked"]:
        if breach_result["compromised"]:
            print(f"  Breach Check       : ⚠ COMPROMISED — seen {breach_result['count']:,} times in breaches")
        else:
            print("  Breach Check       : ✓ Clean — never seen in any breach")
    else:
        print(f"  Breach Check       : – Skipped ({breach_result['reason']})")

    print_separator()