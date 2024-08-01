import csv
import sys


def exit_program():
    print("Goodbye! Program terminated.")
    sys.exit(0)

def move_second_row_to_end(csv_file_path):
    try:
        # Read the CSV file
        data = []
        with open(csv_file_path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)

        if len(data) < 2:
            print("The CSV file does not have a second row to move.")
            return

        # Remove the second row and store it
        second_row = data.pop(1)

        # Append the second row to the end of the data
        data.append(second_row)

        # Write the modified data back to the CSV file
        with open(csv_file_path, 'w', newline='') as updated_csv_file:
            csv_writer = csv.writer(updated_csv_file)
            csv_writer.writerows(data)

        print("The second row has been moved to the end of the CSV file.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def exp_easy():
    try:
        # Ask the user for the name of the source CSV file
        source_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\exp_easy.csv"

        # Read the source CSV file
        data = []
        with open(source_file_path, 'r', newline='') as source_csv_file:
            csv_reader = csv.reader(source_csv_file)
            for row in csv_reader:
                data.append(row)

        if len(data) < 2:
            print("The source CSV file does not have a second row to cut.")
            return

        # Display the second row from the source CSV file
        print(f'\n{data[1]}\n')

        # Ask the user for the name of the destination CSV file
        while True:
            try:
                option = int(input(f"Select one option:\n\n1) More practice\n2) checking\n3) Keep it\n4) Terminate program\n"))
                if option < 1 or option > 4:
                    raise ValueError("You must enter a number between 1 and 3.")
                break
            except ValueError:
                print('Invalid option. Please enter a number from 1 to 3.')

        if option == 1:
            destination_file_name = "exp_more_practice.csv"
        elif option == 2:
            destination_file_name = "exp_checking.csv"
        elif option == 3:
            csv_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\exp_easy.csv" 
            move_second_row_to_end(csv_file_path)
            infinite_exp_easy()

        elif option == 4:
            exit_program()

        # Cut the second row from the source data
        second_row = data.pop(1)

        # Append the second row to the destination CSV file
        with open(destination_file_name, 'a', newline='') as destination_csv_file:
            csv_writer = csv.writer(destination_csv_file)
            csv_writer.writerow(second_row)

        # Update the source CSV file without the second row
        with open(source_file_path, 'w', newline='') as updated_source_csv_file:
            csv_writer = csv.writer(updated_source_csv_file)
            csv_writer.writerows(data)

        print(f"The second row has been added to {destination_file_name} and removed from the source CSV file.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def exp_more_practice():
    try:
        # Ask the user for the name of the source CSV file
        source_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\exp_more_practice.csv"

        # Read the source CSV file
        data = []
        with open(source_file_path, 'r', newline='') as source_csv_file:
            csv_reader = csv.reader(source_csv_file)
            for row in csv_reader:
                data.append(row)

        if len(data) < 2:
            print("The source CSV file does not have a second row to cut.")
            return

        # Display the second row from the source CSV file
        print(f'\n{data[1]}\n')

        # Ask the user for the name of the destination CSV file
        while True:
            try:
                option = int(input(f"Select one option:\n\n1) easy\n2) checking\n3) Keep it\n4) Terminate program\n"))
                if option < 1 or option > 4:
                    raise ValueError("You must enter a number between 1 and 3.")
                break
            except ValueError:
                print('Invalid option. Please enter a number from 1 to 3.')

        if option == 1:
            destination_file_name = "exp_easy.csv"
        elif option == 2:
            destination_file_name = "exp_checking.csv"
        elif option == 3:
            csv_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\exp_more_practice.csv" 
            move_second_row_to_end(csv_file_path)
            infinite_exp_more_practice()

        elif option == 4:
            exit_program()

        # Cut the second row from the source data
        second_row = data.pop(1)

        # Append the second row to the destination CSV file
        with open(destination_file_name, 'a', newline='') as destination_csv_file:
            csv_writer = csv.writer(destination_csv_file)
            csv_writer.writerow(second_row)

        # Update the source CSV file without the second row
        with open(source_file_path, 'w', newline='') as updated_source_csv_file:
            csv_writer = csv.writer(updated_source_csv_file)
            csv_writer.writerows(data)

        print(f"The second row has been added to {destination_file_name} and removed from the source CSV file.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def exp_checking():
    try:
        # Ask the user for the name of the source CSV file
        source_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\exp_checking.csv"

        # Read the source CSV file
        data = []
        with open(source_file_path, 'r', newline='') as source_csv_file:
            csv_reader = csv.reader(source_csv_file)
            for row in csv_reader:
                data.append(row)

        if len(data) < 2:
            print("The source CSV file does not have a second row to cut.")
            return

        # Display the second row from the source CSV file
        
        print(f'\n{data[1]}\n')

        # Ask the user for the name of the destination CSV file
        while True:
            try:
                option = int(input(f"Select one option:\n\n1) easy\n2) more practice\n3) Keep it\n4) Terminate program\n"))
                if option < 1 or option > 4:
                    raise ValueError("You must enter a number between 1 and 3.")
                break
            except ValueError:
                print('Invalid option. Please enter a number from 1 to 3.')

        if option == 1:
            destination_file_name = "exp_easy.csv"
        elif option == 2:
            destination_file_name = "exp_more_practice.csv"
        elif option == 3:
            csv_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\exp_checking.csv" 
            move_second_row_to_end(csv_file_path)
            infinite_exp_checking()


        elif option == 4:
            exit_program()

        # Cut the second row from the source data
        second_row = data.pop(1)

        # Append the second row to the destination CSV file
        with open(destination_file_name, 'a', newline='') as destination_csv_file:
            csv_writer = csv.writer(destination_csv_file)
            csv_writer.writerow(second_row)

        # Update the source CSV file without the second row
        with open(source_file_path, 'w', newline='') as updated_source_csv_file:
            csv_writer = csv.writer(updated_source_csv_file)
            csv_writer.writerows(data)

        print(f"The second row has been added to {destination_file_name} and removed from the source CSV file.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def infinite_exp_easy():
    while True:
        exp_easy()

def infinite_exp_more_practice():
    while True:
        exp_more_practice()
        

def infinite_exp_checking():
    while True:
        exp_checking()

def exp():
    while True:
        try:
            option = int(input("What are you up to?\n\n1) easy\n2) More practice\n3) checking\n4) finish session\n"))
            if option < 1 or option > 4:
                raise ValueError("You must enter a number between 1 and 4.")
        except ValueError:
            print('Invalid option. Please enter a number from 1 to 4.')
            continue

        if option == 1:
            infinite_exp_easy()
        elif option == 2:
            infinite_exp_more_practice()
        elif option == 3:
            infinite_exp_checking()
        elif option == 4:
            print('good work')
            break



##################################

def ph_easy():
    try:
        # Ask the user for the name of the source CSV file
        source_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\ph_easy.csv"

        # Read the source CSV file
        data = []
        with open(source_file_path, 'r', newline='') as source_csv_file:
            csv_reader = csv.reader(source_csv_file)
            for row in csv_reader:
                data.append(row)

        if len(data) < 2:
            print("The source CSV file does not have a second row to cut.")
            return

        # Display the second row from the source CSV file
        print(f'\n{data[1]}\n')

        # Ask the user for the name of the destination CSV file
        while True:
            try:
                option = int(input(f"Select one option:\n\n1) More practice\n2) checking\n3) Keep it\n4) Terminate program\n"))
                if option < 1 or option > 4:
                    raise ValueError("You must enter a number between 1 and 3.")
                break
            except ValueError:
                print('Invalid option. Please enter a number from 1 to 3.')

        if option == 1:
            destination_file_name = "ph_more_practice.csv"
        elif option == 2:
            destination_file_name = "ph_checking.csv"
        elif option == 3:
            csv_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\ph_easy.csv" 
            move_second_row_to_end(csv_file_path)
            infinite_ph_easy()

        elif option == 4:
            exit_program()

        # Cut the second row from the source data
        second_row = data.pop(1)

        # Append the second row to the destination CSV file
        with open(destination_file_name, 'a', newline='') as destination_csv_file:
            csv_writer = csv.writer(destination_csv_file)
            csv_writer.writerow(second_row)

        # Update the source CSV file without the second row
        with open(source_file_path, 'w', newline='') as updated_source_csv_file:
            csv_writer = csv.writer(updated_source_csv_file)
            csv_writer.writerows(data)

        print(f"The second row has been added to {destination_file_name} and removed from the source CSV file.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def ph_more_practice():
    try:
        # Ask the user for the name of the source CSV file
        source_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\ph_more_practice.csv"

        # Read the source CSV file
        data = []
        with open(source_file_path, 'r', newline='') as source_csv_file:
            csv_reader = csv.reader(source_csv_file)
            for row in csv_reader:
                data.append(row)

        if len(data) < 2:
            print("The source CSV file does not have a second row to cut.")
            return

        # Display the second row from the source CSV file
        print(f'\n{data[1]}\n')

        # Ask the user for the name of the destination CSV file
        while True:
            try:
                option = int(input(f"Select one option:\n\n1) easy\n2) checking\n3) Keep it\n4) Terminate program\n"))
                if option < 1 or option > 4:
                    raise ValueError("You must enter a number between 1 and 3.")
                break
            except ValueError:
                print('Invalid option. Please enter a number from 1 to 3.')

        if option == 1:
            destination_file_name = "ph_easy.csv"
        elif option == 2:
            destination_file_name = "ph_checking.csv"
        elif option == 3:
            csv_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\ph_more_practice.csv" 
            move_second_row_to_end(csv_file_path)
            infinite_ph_more_practice()

        elif option == 4:
            exit_program()

        # Cut the second row from the source data
        second_row = data.pop(1)

        # Append the second row to the destination CSV file
        with open(destination_file_name, 'a', newline='') as destination_csv_file:
            csv_writer = csv.writer(destination_csv_file)
            csv_writer.writerow(second_row)

        # Update the source CSV file without the second row
        with open(source_file_path, 'w', newline='') as updated_source_csv_file:
            csv_writer = csv.writer(updated_source_csv_file)
            csv_writer.writerows(data)

        print(f"The second row has been added to {destination_file_name} and removed from the source CSV file.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def ph_checking():
    try:
        # Ask the user for the name of the source CSV file
        source_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\ph_checking.csv"

        # Read the source CSV file
        data = []
        with open(source_file_path, 'r', newline='') as source_csv_file:
            csv_reader = csv.reader(source_csv_file)
            for row in csv_reader:
                data.append(row)

        if len(data) < 2:
            print("The source CSV file does not have a second row to cut.")
            return

        # Display the second row from the source CSV file
        
        print(f'\n{data[1]}\n')

        # Ask the user for the name of the destination CSV file
        while True:
            try:
                option = int(input(f"Select one option:\n\n1) easy\n2) more practice\n3) Keep it\n4) Terminate program\n"))
                if option < 1 or option > 4:
                    raise ValueError("You must enter a number between 1 and 3.")
                break
            except ValueError:
                print('Invalid option. Please enter a number from 1 to 3.')

        if option == 1:
            destination_file_name = "ph_easy.csv"
        elif option == 2:
            destination_file_name = "ph_more_practice.csv"
        elif option == 3:
            csv_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\ph_checking.csv" 
            move_second_row_to_end(csv_file_path)
            infinite_ph_checking()


        elif option == 4:
            exit_program()

        # Cut the second row from the source data
        second_row = data.pop(1)

        # Append the second row to the destination CSV file
        with open(destination_file_name, 'a', newline='') as destination_csv_file:
            csv_writer = csv.writer(destination_csv_file)
            csv_writer.writerow(second_row)

        # Update the source CSV file without the second row
        with open(source_file_path, 'w', newline='') as updated_source_csv_file:
            csv_writer = csv.writer(updated_source_csv_file)
            csv_writer.writerows(data)

        print(f"The second row has been added to {destination_file_name} and removed from the source CSV file.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def infinite_ph_easy():
    while True:
        ph_easy()

def infinite_ph_more_practice():
    while True:
        ph_more_practice()
        

def infinite_ph_checking():
    while True:
        ph_checking()

def ph():
    while True:
        try:
            option = int(input("What are you up to?\n\n1) easy\n2) More practice\n3) checking\n4) finish session\n"))
            if option < 1 or option > 4:
                raise ValueError("You must enter a number between 1 and 4.")
        except ValueError:
            print('Invalid option. Please enter a number from 1 to 4.')
            continue

        if option == 1:
            infinite_ph_easy()
        elif option == 2:
            infinite_ph_more_practice()
        elif option == 3:
            infinite_ph_checking()
        elif option == 4:
            print('good work')
            break


#################


def vr_easy():
    try:
        # Ask the user for the name of the source CSV file
        source_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\vr_easy.csv"

        # Read the source CSV file
        data = []
        with open(source_file_path, 'r', newline='') as source_csv_file:
            csv_reader = csv.reader(source_csv_file)
            for row in csv_reader:
                data.append(row)

        if len(data) < 2:
            print("The source CSV file does not have a second row to cut.")
            return

        # Display the second row from the source CSV file
        print(f'\n{data[1]}\n')

        # Ask the user for the name of the destination CSV file
        while True:
            try:
                option = int(input(f"Select one option:\n\n1) More practice\n2) checking\n3) Keep it\n4) Terminate program\n"))
                if option < 1 or option > 4:
                    raise ValueError("You must enter a number between 1 and 3.")
                break
            except ValueError:
                print('Invalid option. Please enter a number from 1 to 3.')

        if option == 1:
            destination_file_name = "vr_more_practice.csv"
        elif option == 2:
            destination_file_name = "vr_checking.csv"
        elif option == 3:
            csv_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\vr_easy.csv" 
            move_second_row_to_end(csv_file_path)
            infinite_vr_easy()

        elif option == 4:
            exit_program()

        # Cut the second row from the source data
        second_row = data.pop(1)

        # Append the second row to the destination CSV file
        with open(destination_file_name, 'a', newline='') as destination_csv_file:
            csv_writer = csv.writer(destination_csv_file)
            csv_writer.writerow(second_row)

        # Update the source CSV file without the second row
        with open(source_file_path, 'w', newline='') as updated_source_csv_file:
            csv_writer = csv.writer(updated_source_csv_file)
            csv_writer.writerows(data)

        print(f"The second row has been added to {destination_file_name} and removed from the source CSV file.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def vr_more_practice():
    try:
        # Ask the user for the name of the source CSV file
        source_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\vr_more_practice.csv"

        # Read the source CSV file
        data = []
        with open(source_file_path, 'r', newline='') as source_csv_file:
            csv_reader = csv.reader(source_csv_file)
            for row in csv_reader:
                data.append(row)

        if len(data) < 2:
            print("The source CSV file does not have a second row to cut.")
            return

        # Display the second row from the source CSV file
        print(f'\n{data[1]}\n')

        # Ask the user for the name of the destination CSV file
        while True:
            try:
                option = int(input(f"Select one option:\n\n1) easy\n2) checking\n3) Keep it\n4) Terminate program\n"))
                if option < 1 or option > 4:
                    raise ValueError("You must enter a number between 1 and 3.")
                break
            except ValueError:
                print('Invalid option. Please enter a number from 1 to 3.')

        if option == 1:
            destination_file_name = "vr_easy.csv"
        elif option == 2:
            destination_file_name = "vr_checking.csv"
        elif option == 3:
            csv_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\vr_more_practice.csv" 
            move_second_row_to_end(csv_file_path)
            infinite_vr_more_practice()

        elif option == 4:
            exit_program()

        # Cut the second row from the source data
        second_row = data.pop(1)

        # Append the second row to the destination CSV file
        with open(destination_file_name, 'a', newline='') as destination_csv_file:
            csv_writer = csv.writer(destination_csv_file)
            csv_writer.writerow(second_row)

        # Update the source CSV file without the second row
        with open(source_file_path, 'w', newline='') as updated_source_csv_file:
            csv_writer = csv.writer(updated_source_csv_file)
            csv_writer.writerows(data)

        print(f"The second row has been added to {destination_file_name} and removed from the source CSV file.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def vr_checking():
    try:
        # Ask the user for the name of the source CSV file
        source_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\vr_checking.csv"

        # Read the source CSV file
        data = []
        with open(source_file_path, 'r', newline='') as source_csv_file:
            csv_reader = csv.reader(source_csv_file)
            for row in csv_reader:
                data.append(row)

        if len(data) < 2:
            print("The source CSV file does not have a second row to cut.")
            return

        # Display the second row from the source CSV file
        
        print(f'\n{data[1]}\n')

        # Ask the user for the name of the destination CSV file
        while True:
            try:
                option = int(input(f"Select one option:\n\n1) easy\n2) more practice\n3) Keep it\n4) Terminate program\n"))
                if option < 1 or option > 4:
                    raise ValueError("You must enter a number between 1 and 3.")
                break
            except ValueError:
                print('Invalid option. Please enter a number from 1 to 3.')

        if option == 1:
            destination_file_name = "vr_easy.csv"
        elif option == 2:
            destination_file_name = "vr_more_practice.csv"
        elif option == 3:
            csv_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\vr_checking.csv" 
            move_second_row_to_end(csv_file_path)
            infinite_vr_checking()


        elif option == 4:
            exit_program()

        # Cut the second row from the source data
        second_row = data.pop(1)

        # Append the second row to the destination CSV file
        with open(destination_file_name, 'a', newline='') as destination_csv_file:
            csv_writer = csv.writer(destination_csv_file)
            csv_writer.writerow(second_row)

        # Update the source CSV file without the second row
        with open(source_file_path, 'w', newline='') as updated_source_csv_file:
            csv_writer = csv.writer(updated_source_csv_file)
            csv_writer.writerows(data)

        print(f"The second row has been added to {destination_file_name} and removed from the source CSV file.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def infinite_vr_easy():
    while True:
        vr_easy()

def infinite_vr_more_practice():
    while True:
        vr_more_practice()
        

def infinite_vr_checking():
    while True:
        vr_checking()

def vr():
    while True:
        try:
            option = int(input("What are you up to?\n\n1) easy\n2) More practice\n3) checking\n4) finish session\n"))
            if option < 1 or option > 4:
                raise ValueError("You must enter a number between 1 and 4.")
        except ValueError:
            print('Invalid option. Please enter a number from 1 to 4.')
            continue

        if option == 1:
            infinite_vr_easy()
        elif option == 2:
            infinite_vr_more_practice()
        elif option == 3:
            infinite_vr_checking()
        elif option == 4:
            print('good work')
            break

####################################


def ad_easy():
    try:
        # Ask the user for the name of the source CSV file
        source_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\ad_easy.csv"

        # Read the source CSV file
        data = []
        with open(source_file_path, 'r', newline='') as source_csv_file:
            csv_reader = csv.reader(source_csv_file)
            for row in csv_reader:
                data.append(row)

        if len(data) < 2:
            print("The source CSV file does not have a second row to cut.")
            return

        # Display the second row from the source CSV file
        print(f'\n{data[1]}\n')

        # Ask the user for the name of the destination CSV file
        while True:
            try:
                option = int(input(f"Select one option:\n\n1) More practice\n2) checking\n3) Keep it\n4) Terminate program\n"))
                if option < 1 or option > 4:
                    raise ValueError("You must enter a number between 1 and 3.")
                break
            except ValueError:
                print('Invalid option. Please enter a number from 1 to 3.')

        if option == 1:
            destination_file_name = "ad_more_practice.csv"
        elif option == 2:
            destination_file_name = "ad_checking.csv"
        elif option == 3:
            csv_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\ad_easy.csv" 
            move_second_row_to_end(csv_file_path)
            infinite_ad_easy()

        elif option == 4:
            exit_program()

        # Cut the second row from the source data
        second_row = data.pop(1)

        # Append the second row to the destination CSV file
        with open(destination_file_name, 'a', newline='') as destination_csv_file:
            csv_writer = csv.writer(destination_csv_file)
            csv_writer.writerow(second_row)

        # Update the source CSV file without the second row
        with open(source_file_path, 'w', newline='') as updated_source_csv_file:
            csv_writer = csv.writer(updated_source_csv_file)
            csv_writer.writerows(data)

        print(f"The second row has been added to {destination_file_name} and removed from the source CSV file.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def ad_more_practice():
    try:
        # Ask the user for the name of the source CSV file
        source_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\ad_more_practice.csv"

        # Read the source CSV file
        data = []
        with open(source_file_path, 'r', newline='') as source_csv_file:
            csv_reader = csv.reader(source_csv_file)
            for row in csv_reader:
                data.append(row)

        if len(data) < 2:
            print("The source CSV file does not have a second row to cut.")
            return

        # Display the second row from the source CSV file
        print(f'\n{data[1]}\n')

        # Ask the user for the name of the destination CSV file
        while True:
            try:
                option = int(input(f"Select one option:\n\n1) easy\n2) checking\n3) Keep it\n4) Terminate program\n"))
                if option < 1 or option > 4:
                    raise ValueError("You must enter a number between 1 and 3.")
                break
            except ValueError:
                print('Invalid option. Please enter a number from 1 to 3.')

        if option == 1:
            destination_file_name = "ad_easy.csv"
        elif option == 2:
            destination_file_name = "ad_checking.csv"
        elif option == 3:
            csv_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\ad_more_practice.csv" 
            move_second_row_to_end(csv_file_path)
            infinite_ad_more_practice()

        elif option == 4:
            exit_program()

        # Cut the second row from the source data
        second_row = data.pop(1)

        # Append the second row to the destination CSV file
        with open(destination_file_name, 'a', newline='') as destination_csv_file:
            csv_writer = csv.writer(destination_csv_file)
            csv_writer.writerow(second_row)

        # Update the source CSV file without the second row
        with open(source_file_path, 'w', newline='') as updated_source_csv_file:
            csv_writer = csv.writer(updated_source_csv_file)
            csv_writer.writerows(data)

        print(f"The second row has been added to {destination_file_name} and removed from the source CSV file.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def ad_checking():
    try:
        # Ask the user for the name of the source CSV file
        source_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\ad_checking.csv"

        # Read the source CSV file
        data = []
        with open(source_file_path, 'r', newline='') as source_csv_file:
            csv_reader = csv.reader(source_csv_file)
            for row in csv_reader:
                data.append(row)

        if len(data) < 2:
            print("The source CSV file does not have a second row to cut.")
            return

        # Display the second row from the source CSV file
        
        print(f'\n{data[1]}\n')

        # Ask the user for the name of the destination CSV file
        while True:
            try:
                option = int(input(f"Select one option:\n\n1) easy\n2) more practice\n3) Keep it\n4) Terminate program\n"))
                if option < 1 or option > 4:
                    raise ValueError("You must enter a number between 1 and 3.")
                break
            except ValueError:
                print('Invalid option. Please enter a number from 1 to 3.')

        if option == 1:
            destination_file_name = "ad_easy.csv"
        elif option == 2:
            destination_file_name = "ad_more_practice.csv"
        elif option == 3:
            csv_file_path = r"C:\Users\Alexandra la Mejor\Desktop\english tools\ad_checking.csv" 
            move_second_row_to_end(csv_file_path)
            infinite_ad_checking()


        elif option == 4:
            exit_program()

        # Cut the second row from the source data
        second_row = data.pop(1)

        # Append the second row to the destination CSV file
        with open(destination_file_name, 'a', newline='') as destination_csv_file:
            csv_writer = csv.writer(destination_csv_file)
            csv_writer.writerow(second_row)

        # Update the source CSV file without the second row
        with open(source_file_path, 'w', newline='') as updated_source_csv_file:
            csv_writer = csv.writer(updated_source_csv_file)
            csv_writer.writerows(data)

        print(f"The second row has been added to {destination_file_name} and removed from the source CSV file.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


def infinite_ad_easy():
    while True:
        ad_easy()

def infinite_ad_more_practice():
    while True:
        ad_more_practice()
        

def infinite_ad_checking():
    while True:
        ad_checking()

def ad():
    while True:
        try:
            option = int(input("What are you up to?\n\n1) easy\n2) More practice\n3) checking\n4) finish session\n"))
            if option < 1 or option > 4:
                raise ValueError("You must enter a number between 1 and 4.")
        except ValueError:
            print('Invalid option. Please enter a number from 1 to 4.')
            continue

        if option == 1:
            infinite_ad_easy()
        elif option == 2:
            infinite_ad_more_practice()
        elif option == 3:
            infinite_ad_checking()
        elif option == 4:
            print('good work')
            break


def eng_main_tool():
    while True:
        try:
            option = int(input("What would you like to do today?\n\n1) expressions\n2) phrasal verbs\n3) verbs\n4) adjectives\n"))
            if option < 1 or option > 4:
                raise ValueError("You must enter a number between 1 and 4.")
        except ValueError:
            print('Invalid option. Please enter a number from 1 to 4.')
            continue

        if option == 1:
            exp()
        elif option == 2:
            ph()
        elif option == 3:
            vr()
        elif option == 4:
            ad()
            

eng_main_tool()
