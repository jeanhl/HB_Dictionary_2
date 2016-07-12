def sorted_restaurant_ratings(filepath):
    filename = open(filepath)
    restaurants_and_ratings = {}
    restaurants = []

    for line in filename:
        new_lines = line.rstrip()
        new_line_list = new_lines.split(":")
        restaurant_name = new_line_list[0]
        restaurant_rating = new_line_list[1]
        print restaurant_name, restaurant_rating
        # restaurants = restaurants + new_lines.split(":")
        # for item in restaurants:
        #     restaurants_and_ratings[item[0]] = item[1]

    # for index in range(0,len(restaurants),2):
    #      restaurants_and_ratings[restaurants[index]] = restaurants[index+1]

    ordered_restaurants = sorted(restaurants_and_ratings)

    for rest in ordered_restaurants:
        ratings = restaurants_and_ratings[rest]
        print "{}, is rated at {}".format(rest, ratings)

print sorted_restaurant_ratings("scores.txt")