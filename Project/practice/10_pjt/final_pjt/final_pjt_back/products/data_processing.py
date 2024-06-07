import pandas as pd
import numpy as np
from products.models import DepositProducts, DepositOptions
from django.contrib.auth import get_user_model

def get_user_ids():
    users = get_user_model().objects.all()
    userIds = [x.id for x in users]
    return userIds

def get_product_data():
    products = DepositProducts.objects.all().values()
    options = DepositOptions.objects.all().values()
    
    product_df = pd.DataFrame(products)
    option_df = pd.DataFrame(options)


    # Merge product and option data on fin_prdt_cd
    merged_df = pd.merge(product_df, option_df, on='fin_prdt_cd')
    data = merged_df[['fin_prdt_cd', 'kor_co_nm', 'fin_prdt_nm', 'intr_rate', 'intr_rate2', 'save_trm']]
    data = data.copy()
    
    users = get_user_ids()
    repeated_user_ids = users * (len(data) // len(users)) + users[:len(data) % len(users)]
    assert len(repeated_user_ids) == len(data)
    data.loc[:,'user_id'] = repeated_user_ids

    np.random.seed(0)  # For reproducibility
    data.loc[:, 'rating'] = np.random.randint(1, 6, len(data))

    return data
