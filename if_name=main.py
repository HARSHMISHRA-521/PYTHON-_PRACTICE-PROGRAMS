def main():
    # Code to be run when the script is run directly
    print("Running script directly")

if __name__ == "__main__":
    main()


    def main():
        print("Running script directly")


    if __name__ == "__main__":
        main()

        import script

        script.main()  # Output: "Running script directly"
        

# In summary, the if __name__ == "__main__" idiom is a common pattern used in Python scripts
# to determine whether the script is being run directly or being imported as
# a module into another script. It allows you to reuse code from a script by importing it as a
# module into another script, without running the code in the original script.