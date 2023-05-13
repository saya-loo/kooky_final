
def average_rating(rating):

    if not rating:

        return 0

    return round(sum(rating) / len(rating))
