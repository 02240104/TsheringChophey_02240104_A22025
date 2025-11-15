def linear_search_student_id(student_list, target_id):
    """
    Perform linear search to find a student ID in the list
    Returns position (1-indexed) and number of comparisons
    """
    comparisons = 0
    for i in range(len(student_list)):
        comparisons += 1
        if student_list[i] == target_id:
            return i + 1, comparisons 
    return -1, comparisons  

def binary_search_score(score_list, target_score):
    """
    Perform binary search to find a score in the sorted list
    Returns position (1-indexed) and number of comparisons
    """
    comparisons = 0
    left = 0
    right = len(score_list) - 1
    
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        
        if score_list[mid] == target_score:
            return mid + 1, comparisons  
        elif score_list[mid] < target_score:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons 

def main():
    student_ids = [2240104, 2240105, 2240106, 2240107, 2240108, 2240109, 2240110, 2240111, 
                   2240112, 2240113, 2240114, 2240115, 2240116, 2240117, 2240118, 2240119, 
                   2240120, 2240121, 2240122, 2240123]
    

    test_scores = [45, 52, 58, 63, 67, 72, 75, 78, 82, 85, 
                   88, 90, 92, 95, 98, 100, 40, 54, 52, 95]
    
    print("Searching Algorithms Program")
    print("Created by: [Tshering Chophey]")
    print()
    
    while True:
        print("Searching Algorithms Menu")
        print("Select a search operation (1-3):")
        print("1. Linear Search - Find Student ID")
        print("2. Binary Search - Find Score")
        print("3. Exit program")
        print()
        
        try:
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                print(f"\nSearching in student IDs: {student_ids}")
                try:
                    target_id = int(input("Enter Student ID to search: "))
                    position, comparisons = linear_search_student_id(student_ids, target_id)
                    
                    if position != -1:
                        print(f"Result: Student ID {target_id} found at position {position}")
                    else:
                        print(f"Result: Student ID {target_id} not found")
                    print(f"Comparisons made: {comparisons}")
                    
                except ValueError:
                    print("Error: Please enter a valid number for Student ID")
            
            elif choice == '2':
                print(f"\nSearching in sorted scores: {test_scores}")
                try:
                    target_score = int(input("Enter score to search: "))
                    position, comparisons = binary_search_score(test_scores, target_score)
                    
                    if position != -1:
                        print(f"Result: Score {target_score} found at position {position}")
                    else:
                        print(f"Result: Score {target_score} not found")
                    print(f"Comparisons made: {comparisons}")
                    
                except ValueError:
                    print("Error: Please enter a valid number for score")
            
            elif choice == '3':
                print("\nThank you for using the search program! Goodbye!")
                break
            
            else:
                print("Invalid choice! Please enter 1, 2, or 3")
            
            if choice in ['1', '2']:
                continue_choice = input("\nWould you like to perform another search? (y/n): ").strip().lower()
                if continue_choice != 'y':
                    print("\nThank you for using the search program! Goodbye!")
                    break
                print()
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()