!git clone https://github.com/SHUBHAMGAWADE7798/outfit-recommender-.git
%cd outfit-recommender

!mkdir -p data
with open("data/outfits.csv", "w") as f:
    f.write("outfit,color,occasion\n")
    f.write("Casual Shirt and Jeans,Blue,Casual\n")
    f.write("Black Suit,Black,Formal\n")
    f.write("Red Dress,Red,Party\n")
    f.write("Sports Tracksuit,Grey,Sports\n")
!cat data/outfits.csv

# Step 4: Create recommender/outfit_recommender.py

# Make sure the recommender directory exists
!mkdir -p recommender

# Create outfit_recommender.py with the recommender class
with open("recommender/outfit_recommender.py", "w") as f:
    f.write("""
import pandas as pd

class OutfitRecommender:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def recommend(self, color=None, occasion=None):
        result = self.data
        if color:
            result = result[result['color'].str.lower() ==
color.lower()]
        if occasion:
            result = result[result['occasion'].str.lower() ==
occasion.lower()]
        return result['outfit'].tolist()
""")

# Write the main.py file in the current directory
with open("main.py", "w") as f:
    f.write("""
from recommender.outfit_recommender import OutfitRecommender
def main():
    recommender = OutfitRecommender("data/outfits.csv")
    print("Recommendations for color='Red', occasion='Party':")
    print(recommender.recommend(color='Red', occasion='Party'))
if __name__ == "__main__":
    main()
""")

!python main.py

!git config --global user.email "shubhamgawade231@gmail.com"
!git config --global user.name "SHUBHAMGAWADE7798"

!git status

!git add .

# Commit changes
!git commit -m "Initial recommender version"
