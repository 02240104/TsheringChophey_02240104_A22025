class QuickSortCounter:
    """Helper class to count recursive calls in quicksort"""
    def __init__(self):
        self.count = 0

def bubble_sort_names(name_list):
    """
    Sort student names alphabetically using bubble sort
    Returns sorted list
    """
    names = name_list.copy()  
    n = len(names)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if names[j] > names[j + 1]:
                names[j], names[j + 1] = names[j + 1], names[j]
    
    return names

def insertion_sort_scores(score_list):
    """
    Sort test scores in ascending order using insertion sort
    Returns sorted list
    """
    scores = score_list.copy()  
    for i in range(1, len(scores)):
        key = scores[i]
        j = i - 1
        
        while j >= 0 and key < scores[j]:
            scores[j + 1] = scores[j]
            j -= 1
        scores[j + 1] = key
    
    return scores

def quick_sort_prices(price_list, counter=None):
    """
    Sort book prices in ascending order using quick sort
    Returns sorted list and number of recursive calls
    """
    if counter is None:
        counter = QuickSortCounter()
    
    if len(price_list) <= 1:
        return price_list, counter.count
    
    counter.count += 1
    
    pivot = price_list[len(price_list) // 2]
    left = [x for x in price_list if x < pivot]
    middle = [x for x in price_list if x == pivot]
    right = [x for x in price_list if x > pivot]
    
    left_sorted, _ = quick_sort_prices(left, counter)
    right_sorted, _ = quick_sort_prices(right, counter)
    
    return left_sorted + middle + right_sorted, counter.count

def main():
    
    student_names = ["Saurez", "Ramous", "Ronaldo", "Neymar", "Ozil", "Pele", "Cryuff", 
                    "Son", "Yamal", "Messi", "Maradona", "Henry", "Mbappe", "Bale", "Haaland"]
    
    
    test_scores = [78, 45, 92, 67, 88, 54, 73, 82, 91, 59, 
                   76, 85, 48, 93, 71, 89, 57, 80, 69, 95]
    
   
    book_prices = [450, 230, 678, 125, 890, 345, 567, 234, 789, 123, 
                   456, 678, 299, 399, 599]
    
    print("=== Sorting Algorithms Program ===")
    print("Created by: [Tshering Chophey]")
    print()
    
    while True:
        print("Sorting Algorithms Menu")
        print("Select a sorting operation (1-4):")
        print("1. Bubble Sort - Sort Student Names")
        print("2. Insertion Sort - Sort Test Scores")
        print("3. Quick Sort - Sort Book Prices")
        print("4. Exit program")
        print()
        
        try:
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                print(f"\nOriginal student names: {student_names}")
                print("\nPerforming Bubble Sort...")
                sorted_names = bubble_sort_names(student_names)
                print(f"Sorted names: {sorted_names}")
            
            elif choice == '2':
                print(f"\nOriginal test scores: {test_scores}")
                print("\nPerforming Insertion Sort...")
                sorted_scores = insertion_sort_scores(test_scores)
                print(f"Sorted scores: {sorted_scores}")
                
                print("\nTop 5 Scores:")
                top_5 = sorted_scores[-5:][::-1]  
                for i, score in enumerate(top_5, 1):
                    print(f"{i}. {score}")
            
            elif choice == '3':
                print(f"\nOriginal book prices: {book_prices}")
                print("\nPerforming Quick Sort...")
                sorted_prices, recursive_calls = quick_sort_prices(book_prices)
                print(f"Sorted prices: {sorted_prices}")
                print(f"Recursive calls: {recursive_calls}")
            
            elif choice == '4':
                print("\nThank you for using the sorting program! Goodbye!")
                break
            
            else:
                print("Invalid choice! Please enter 1, 2, 3, or 4")
            
           
            if choice in ['1', '2', '3']:
                continue_choice = input("\nWould you like to perform another sort? (y/n): ").strip().lower()
                if continue_choice != 'y':
                    print("\nThank you for using the sorting program! Goodbye!")
                    break
                print()
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()