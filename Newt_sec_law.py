#!/user/bin/env.python3
# Created By: Jeremiah omoike
# Date: Dec 1, 2022
# This program utilizes newtons second law (Force = mass x acceleration). The program asks user for the missing variable that they want to solve for and then asks for user inputs to solve for the missing variable.

def calc_force( mass, acceleration):
    force = mass * acceleration
    return force
    
def calc_mass(force, acceleration):
    mass = force / acceleration
    return mass

def calc_acceleration(force, mass):
    acceleration = force / mass
    return acceleration
def main():
        solve_for_user = input("What would you like to solve for. (input f for force, m for mass and a for acceleration): ")
        if solve_for_user == "f" or solve_for_user == "m" or solve_for_user == "a":
            if solve_for_user == "f":
                print()
                print("Force = mass * acceleration")
                print()
                while solve_for_user == "f":
                    mass_user = input("Enter mass(g): ")
                    try:
                        mass_float = float(mass_user)

                        acceleration_user = input("Enter acceleration(m/s^2): ")
                        try:
                            acceleration_float = float(acceleration_user)
                            force_user = calc_force(mass_float, acceleration_float)
                            print()
                            print("The force of an object with a mass of {} g and moving at an accelerating pace of {} m/s^2 is {:.2f} N.".format(mass_float, acceleration_float, force_user))
                            break
                        except Exception:
                            print()
                            print("{} is not a number.".format(acceleration_user))
                            print()
                            print("Try again")
                            continue
                    except Exception:
                        print()
                        print("{} is not a number.".format(mass_user))
                        print()
                        print("Try again")
                        continue
    
            elif solve_for_user == "m":
                print()
                print("Mass = force / acceleration")
                print()
                while solve_for_user == "m":
                    force_user = input("Enter force(N): ")
                    try:
                        force_float = float(force_user)
                
                        print()
                        acceleration_user = input("Enter acceleration(m/s^2): ")
                        try:
                            acceleration_float = float(acceleration_user)
                
                            mass_user = calc_mass( force_float, acceleration_float)
                            print()
                            print("The mass of an object moving at an accelerating pace of {} m/s^2, with the force of {} N is {:.2f} g. ".format(acceleration_float, force_float, mass_user))
                            break
                        except Exception:
                            print()
                            print("{} is not a number.".format(acceleration_user))
                            print()
                            print("Try again")
                            continue
                    except Exception:
                        print()
                        print("{} is not a number.".format(force_user))
                        print()
                        print("Try again")
                        continue
            elif solve_for_user == "a":
                print()
                print("Acceleration = Force / mass")
                print()
                while solve_for_user == "a":
                    force_user = input("Enter force(N): ")
                    try:
                        force_float = float(force_user)
                        mass_user = input("Enter mass(g): ")
                        try:
                            mass_float = float(mass_user)
                            acceleration_user = calc_acceleration(force_float, mass_float)
                            print()
                            print("The acceleration of a moving object that has the mass of {} g and the force of {} N is {:.2f}m/s^2. ".format(mass_float, force_float, acceleration_user))
                            break
                        except Exception:
                            print()
                            print("{} is not a number".format(mass_user))
                            print()
                            print("Try again")
                            continue
                    except Exception:
                        print()
                        print("{} is not a number.".format(force_user))
                        print()
                        print("Try again")
                        continue
        else:
            print()
            print("You cannot solve for {}".format(solve_for_user))
            print()
            
            

if __name__ == "__main__":
    main()
