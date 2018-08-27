
# Adding some pandas notes from this Notebook (https://www.kaggle.com/adityapatil673/visual-analysis-of-apps-on-applestore):

# reducing the number of categories

s = data.prime_genre.value_counts().index[:4]
def categ(x):
    if x in s:
        return x
    else :
        return "Others"

data['broad_genre']= data.prime_genre.apply(lambda x : categ(x))


free = data[data.price==0].broad_genre.value_counts().sort_index().to_frame()
paid = data[data.price>0].broad_genre.value_counts().sort_index().to_frame()
total = data.broad_genre.value_counts().sort_index().to_frame()

# Create a new df (?):
free.columns=['free']
paid.columns=['paid']
total.columns=['total']
dist = free.join(paid).join(total)
dist ['paid_per'] = dist.paid*100/dist.total
dist ['free_per'] = dist.free*100/dist.total
dist


# Add a column:
def paid(x):
    if x>0:
        return 'Paid'
    else :
        return'Free'

data['category']= data.price.apply(lambda x : paid(x))
data.tail()



# Violin plots!
plt.figure(figsize=(15,8))
plt.style.use('fast')
plt.ylim([0,5])
plt.title("Distribution of User ratings")
sns.violinplot(data=data, y ='user_rating',x='broad_genre',hue='category',
               vertical=True,kde=False,split=True ,linewidth=2,
               scale ='count', palette=['#fdd470','#45cea2'])


# Great colors:
flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]


# Preparing...for a regression plot?
paidapps_regression =data[((data.price<30) & (data.price>0))]
sns.lmplot(data=paidapps_regression,
           x='MB',y='price',size=4, aspect=2,col_wrap=2,hue='broad_genre',
           col='broad_genre',fit_reg=False,palette = sns.color_palette("husl", 5))
plt.show()



# All in all, it would definitely pay to know matplotlib subfigure syntax...

# Yeah, we should get comfortable with SNS plotting, matplotlib plotting, Dash plotting, ...
