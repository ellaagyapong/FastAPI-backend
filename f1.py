# MTN MoMo Balance Checker - Simulation

PIN = "2345"
BALANCE = 1247.50

while True:
    print("\nMTN MoMo Balance Checker")
    print("1) Dial *170#")
    print("2) Exit")

    choice = input("\nSelect an option: ")

    if choice == "1":
        print("\nDialling *170#...")
        print("\nUnlock more deals, try our new MoMo App")
        print("1) Transfer Money")
        print("2) MoMoPay& Pay Bill")
        print("3) Airtime& Bundles")
        print("4) Allow Cash Out")
        print("5) Financial")
        print("# for next")

        reply = input("\nReply: ")

        if reply == "#":
            print("\nServices")
            print("6) My Wallet")
            print("7) Just4U Offers for you")
            print("8) MoMo App (300MB free data)")

            reply = input("\nReply: ")

            if reply == "6":
                print("\nMy Wallet")
                print("1) Check Balance")
                print("2) Allow Cash Out")
                print("3) My Approvals")
                print("4) Report Fraud")
                print("5) Statements")
                print("6) Change PIN")
                print("7) Upgrade Profile Type")
                print("8) Reversals")
                print("9) Check Wallet Limits")
                print("0) Back")

                reply = input("\nReply: ")

                if reply == "1":
                    print("\nFee is GHS 0.00. Enter MM PIN: ", end="")
                    entered_pin = input()

                    if entered_pin == PIN:
                        print(f"\nYour MoMo balance is GHS {BALANCE:,.2f}.")
                    else:
                        print("\nIncorrect PIN.")
                        print("Transaction cancelled.")

                elif reply == "0":
                    continue

                else:
                    print("\nInvalid option.")

            else:
                print("\nInvalid option.")

        else:
            print("\nInvalid option.")

    elif choice == "2":
        print("\nThank you for using MTN Mobile Money.")
        break

    else:
        print("\nInvalid option. Please select 1 or 2.")