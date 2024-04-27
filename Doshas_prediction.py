import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf

print(tf.__version__)

def load_model():
    vat_model = tf.keras.models.load_model('trained_models/vata_model.keras')
    pit_model = tf.keras.models.load_model('trained_models/pitta_model.keras')
    kp_model = tf.keras.models.load_model('trained_models/kapha_model.keras')
    return vat_model, pit_model, kp_model

vat_model, pit_model, kp_model = load_model()

def show_predict_page():
    st.set_page_config(page_title='Find your Dosha', layout="wide", initial_sidebar_state="expanded")
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://wallpaperaccess.com/full/1603870.png");
    background-size: cover;
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    heavy = 0
    medium = 0
    thin = 0

    dont_gain_weight_easily = 0
    dont_lose_weight_easily = 0
    gain_and_lose_weight_easily = 0

    inconsistent_appetite = 0
    appetite_steady_appetite = 0
    strong_appetite_cant_skip_meal = 0 

    light_restless_sleep = 0
    heavy_sleep = 0 
    moderate_good_sleep =0 

    neither_or_both = 0
    weather_prefer_cold = 0
    weather_prefer_warmth = 0 

    dry_frizzy_hair = 0
    fine_thin_hairs = 0
    thick_and_oily = 0

    gets_irritated = 0
    under_stress_is_anxious_and_worried = 0 
    behaviour_withdrawn = 0

    dry_and_rough_skin = 0
    thick_and_oily = 0
    warm_reddish_and_irritable = 0 

    cold_hands_and_feet = 0 
    body_normal = 0 
    body_warm_body = 0

    easy_going_and_adaptive = 0
    workflow_lively_and_enthusiastic = 0 
    workflow_purposeful_and_intense = 0

    array_of_features = [thin, medium, heavy, dont_gain_weight_easily, gain_and_lose_weight_easily, dont_lose_weight_easily, inconsistent_appetite, strong_appetite_cant_skip_meal, appetite_steady_appetite, light_restless_sleep, moderate_good_sleep, heavy_sleep, weather_prefer_warmth, weather_prefer_cold, neither_or_both, dry_frizzy_hair, fine_thin_hairs,thick_and_oily, under_stress_is_anxious_and_worried, gets_irritated, behaviour_withdrawn, dry_and_rough_skin, warm_reddish_and_irritable, thick_and_oily, cold_hands_and_feet, body_warm_body, body_normal, workflow_lively_and_enthusiastic, workflow_purposeful_and_intense, easy_going_and_adaptive]
    tab1, tab2 = st.tabs(["Dosh Test", "Diet"])
    
    with tab1:
        st.header('**Find your Dosha**:dna:')
        st.divider()
        col1, col2 = st.columns(2)
        col1.subheader("**1. Weight**:man-lifting-weights:")
        Body = col2.radio("**Weight**:man-lifting-weights:",["None", "Light Weight","Muscular", "Heavy Weight"], label_visibility="collapsed", horizontal= True)
        st.divider()
        col3, col4 = st.columns(2)
        col3.subheader("**2. Weight Gain and Loss**:green_salad:")
        Weight_Loss = col4.radio("**Weight Gain and Loss**:green_salad:", ["None", "Can't gain weight easily", "Can't loose weight easily", "gain or loose weight easily"],label_visibility="collapsed", horizontal= True)
        st.divider()
        col5, col6 = st.columns(2)
        col5.subheader("**3. Appetite**:stuffed_flatbread:")
        Appetite = col6.radio("**Appetite**:stuffed_flatbread:",["None", "Inconsistent appetite", "Steady appetite", "Strong appetite"], label_visibility="collapsed", horizontal= True)
        st.divider()
        col7, col8 = st.columns(2)
        col7.subheader("**Sleeping Behavior**:sleeping:")
        Sleeping_behaviour = col8.radio("**Sleeping Behavior**:sleeping:", ["None", "Light Sleeper", "Heavy Sleeper", "Moderate Sleeper"], label_visibility="collapsed", horizontal= True)
        st.divider()
        col9, col10 = st.columns(2)
        col9.subheader("**Favourite Season**:sunny::cloud:")
        Favourite_Season = col10.radio("**Favourite Season**:sunny::cloud:", ["None", "Like all seasons", "Winter", "Summer"], label_visibility="collapsed", horizontal= True)
        st.divider()
        col11, col12 = st.columns(2)
        col11.subheader("**Type of Hair**:curly_haired_man:")
        Hair_Type = col12.radio("**Type of Hair**:curly_haired_man:", ["None", "Dry Frizzy Hair", "Fine Thin Hair", "Thick and Oily Hair"], label_visibility="collapsed", horizontal= True)
        st.divider()
        col13, col14 = st.columns(2)
        col13.subheader("**Nature**:innocent:")
        Nature = col14.radio("**Nature**:innocent:", ["None", "Irritated", "Anxious and Worried", "Withdrawn from Life"], label_visibility="collapsed", horizontal= True)
        st.divider()
        col15, col16 = st.columns(2)
        col15.subheader("**Skin Type**:man:")
        Skin = col16.radio("**Skin Type**:man:", ["None", "Dry and Rough", "Thick and Oily", "Reddish and Itchy"], label_visibility="collapsed", horizontal= True)
        st.divider()
        col17, col18 = st.columns(2)
        col17.subheader("**Body Temperature**:male-doctor:")
        Body_Temperature = col18.radio("**Body Temperature**:male-doctor:", ["None", "Cold", "Normal", "Warm"], label_visibility="collapsed", horizontal= True)
        st.divider()
        col19, col20 = st.columns(2)
        col19.subheader("**Workflow**:man-juggling:")
        Workflow = col20.radio("**Workflow**:man-juggling:", ["None", "Easy going and Adaptive", "Lively and Enthusiastic", "Purposeful and Intense"],label_visibility="collapsed", horizontal= True)
        st.divider()
    
    with tab2:
        con = st.container()
        if (Workflow or Body_Temperature or Skin or Nature or Hair_Type or Favourite_Season or Sleeping_behaviour or Appetite or Weight_Loss or Body):
            if Body == "Light Weight": array_of_features[0] = 1
            elif Body == "Muscular": array_of_features[1] = 1
            elif Body == "Heavy Weight": array_of_features[2] = 1
            
            if Weight_Loss == "Can't gain weight easily": array_of_features[3] = 1
            elif Weight_Loss == "gain or loose weight easily": array_of_features[4] = 1
            elif Weight_Loss == "Can't loose weight easily": array_of_features[5] = 1
            
            if Appetite == "Inconsistent appetite": array_of_features[6] = 1
            elif Appetite == "Steady appetite": array_of_features[7] = 1
            elif Appetite == "Strong appetite": array_of_features[8] = 1

            if Sleeping_behaviour == "Light Sleeper": array_of_features[9] = 1
            elif Sleeping_behaviour == "Moderate Sleeper": array_of_features[10] = 1
            elif Sleeping_behaviour ==  "Heavy Sleeper": array_of_features[11] = 1
            
            if Favourite_Season == "Summer": array_of_features[12] = 1
            elif Favourite_Season == "Winter": array_of_features[13] = 1
            elif Favourite_Season == "Like all seasons": array_of_features[14] = 1

            if Hair_Type == "Dry Frizzy Hair" : array_of_features[15] = 1
            elif Hair_Type == "Fine Thin Hair": array_of_features[16] = 1
            elif Hair_Type == "Thick and Oily Hair": array_of_features[17] = 1
            
            if Nature == "Anxious and Worried": array_of_features[18] = 1
            elif Nature == "Irritated": array_of_features[19] = 1
            elif Nature == "Withdrawn from Life": array_of_features[20] = 1
            
            if Skin == "Dry and Rough": array_of_features[21] = 1
            elif Skin == "Reddish and Itchy": array_of_features[22] = 1
            elif Skin == "Thick and Oily": array_of_features[23] = 1
            
            if Body_Temperature == "Cold": array_of_features[24] = 1
            elif Body_Temperature == "Warm": array_of_features[25] = 1
            elif Body_Temperature == "Normal": array_of_features[26] = 1
            
            if Workflow == "Lively and Enthusiastic": array_of_features[27] = 1
            elif Workflow == "Easy going and Adaptive": array_of_features[29] = 1
            elif Workflow == "Purposeful and Intense" : array_of_features[28] = 1
            
            # print(array_of_features)
            if (array_of_features != [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]):
                array_of_features = pd.DataFrame([array_of_features])
                a = np.round(vat_model.predict(array_of_features), 2)
                b = np.round(pit_model.predict(array_of_features), 2)
                c = np.round(kp_model.predict(array_of_features), 2)
                
                a_percent = a[0][1]/(a[0][1] + b[0][1] + c[0][1])
                b_percent = b[0][1]/(a[0][1] + b[0][1] + c[0][1])
                c_percent = c[0][1]/(a[0][1] + b[0][1] + c[0][1])
            else:
                a_percent = 0.05
                b_percent = 0.05
                c_percent = 0.05

            with st.sidebar:
                st.header('**Dosha Imbalance**:dna:')
                st.progress(int(a_percent*99.9), text="Vata")
                st.progress(int(b_percent*99.9), text="Pitta")
                st.progress(int(c_percent*99.9), text="Kapha")
                if(a_percent>b_percent and a_percent > c_percent):
                    con.subheader("It is likely for you to have **Vata** Dosha")
                    html_string  = "<h2>Vata-Balancing Diet: Foods to Favor and Limit</h2><p>The following table provides a guideline for incorporating Vata-balancing foods into your diet:</p><table><tr><th>Category</th><th>Foods to Favor</th><th>Foods to Limit</th></tr><tr><td>Grains</td><td>Oats, basmati rice, quinoa, wheat</td><td>Dry or processed grains (corn, barley)</td></tr><tr><td>Vegetables</td><td>Cooked root vegetables (sweet potatoes, carrots, beets), green beans, squash, zucchini, asparagus</td><td>Raw vegetables (in excess), cruciferous vegetables (broccoli, cauliflower)</td></tr><tr><td>Fruits</td><td>Sweet, moist fruits (dates, figs, grapes, mangoes, pears, bananas, berries)</td><td>Sour fruits (cranberries, pomegranates), dried fruits (except raisins)</td></tr><tr><td>Proteins</td><td>Eggs, chicken, turkey, fish (in moderation)</td><td>Processed meats, red meat (limited)</td></tr><tr><td>Dairy</td><td>Milk, ghee, yogurt (fresh)</td><td>Cold dairy products (iced drinks, yogurt)</td></tr><tr><td>Nuts & Seeds</td><td>Almonds, walnuts, cashews, flaxseeds</td><td>Light nuts (peanuts)</td></tr><tr><td>Oils</td><td>Ghee, olive oil, coconut oil, sesame oil</td><td>Light oils (corn, canola)</td></tr><tr><td>Beverages</td><td>Warm water, herbal teas, buttermilk (moderation)</td><td>Cold drinks (iced water, carbonated beverages), excessive coffee or alcohol</td></tr></table><p>Remember, this is a general guide. Consult an Ayurvedic practitioner for a personalized plan based on your specific needs.</p>"
                    con.markdown(html_string, unsafe_allow_html=True)
                elif(a_percent<b_percent and b_percent > c_percent):
                    con.subheader("It is likely for you to have **Pitta** Dosha")
                    html_string  = "<h2>Pitta-Balancing Diet: Foods to Favor and Limit</h2><p>The following table provides a guideline for incorporating Pitta-balancing foods into your diet:</p><table><tr><th>Category</th><th>Foods to Favor</th><th>Foods to Limit</th></tr><tr><td>Grains</td><td>Basmati rice, barley, wheat (moderation)</td><td>-</td></tr><tr><td>Vegetables</td><td>Leafy greens (spinach, kale), asparagus, cucumber, zucchini, broccoli, cauliflower</td><td>Spicy vegetables (peppers), tomatoes</td></tr><tr><td>Fruits</td><td>Sweet fruits (melons, pears, apples, grapes, berries)</td><td>Sour fruits (citrus, grapefruit), dried fruits (except raisins)</td></tr><tr><td>Proteins</td><td>Lean proteins (chicken, fish, lentils, mung beans)</td><td>Red meat, processed meats</td></tr><tr><td>Dairy</td><td>Yogurt (sweet or buttermilk), milk (moderation)</td><td>Cheese (aged), excessive cheese consumption</td></tr><tr><td>Nuts & Seeds</td><td>Almonds, pumpkin seeds, sunflower seeds (moderation)</td><td>Cashews, peanuts</td></tr><tr><td>Oils</td><td>Coconut oil, ghee (moderation), olive oil</td><td>Fried foods, vegetable oils (heavy processing)</td></tr><tr><td>Beverages</td><td>Cool water, coconut water, herbal teas (licorice, peppermint)</td><td>Coffee, alcohol, sugary drinks</td></tr></table><p>Remember, this is a general guide. Consult an Ayurvedic practitioner for a personalized plan based on your specific needs.</p>"
                    con.markdown(html_string, unsafe_allow_html=True)
                elif(c_percent>b_percent and a_percent < c_percent):
                    con.subheader("It is likely for you to have **Kapha** Dosha")
                    html_string  = "<h2>Kapha-Balancing Diet: Foods to Favor and Limit</h2><p>The following table provides a guideline for incorporating Kapha-balancing foods into your diet:</p><table><tr><th>Category</th><th>Foods to Favor</th><th>Foods to Limit</th></tr><tr><td>Grains</td><td>Lighter grains (barley, millet, buckwheat)</td><td>Wheat (limited), heavy or processed grains (oats, rice)</td></tr><tr><td>Vegetables</td><td>Arugula, leafy greens (except collard greens), asparagus, celery, cruciferous vegetables (broccoli, cauliflower)</td><td>Sweet and starchy vegetables (potatoes, corn, peas), nightshade vegetables (tomatoes, eggplant)</td></tr><tr><td>Fruits</td><td>Pungent or tart fruits (apples, pears, cranberries, pomegranates)</td><td>Sweet and juicy fruits (bananas, mangoes, grapes, melons)</td></tr><tr><td>Proteins</td><td>Lean proteins (chicken, turkey, fish, lentils)</td><td>Fatty meats (red meat, lamb), dairy (except small amounts)</td></tr><tr><td>Spices</td><td>Warming spices (ginger, cumin, turmeric, black pepper, chili peppers)</td><td>Sweet and cooling spices (fennel, coriander, cardamom)</td></tr><tr><td>Oils</td><td>Mustard oil, sunflower oil, safflower oil</td><td>Ghee, coconut oil, heavy oils</td></tr><tr><td>Beverages</td><td>Warm water with lemon or ginger, herbal teas (especially ginger or dandelion)</td><td>Cold drinks, sugary drinks, dairy milk (except small amounts)</td></tr</table><p>Remember, this is a general guide. Consult an Ayurvedic practitioner for a personalized plan based on your specific needs.</p>"
                    con.markdown(html_string, unsafe_allow_html=True)
                elif(a_percent == b_percent and a_percent!=c_percent):
                    con.subheader("It is likely for you to have both **Vata & Pitta** Dosha")
                    html_string  = "<h2>Pitta-Vata Balancing Diet: Foods to Favor and Limit</h2><p>The following table provides a guideline for incorporating Pitta-Vata balancing foods into your diet. Remember, this is a general guide, and consulting an Ayurvedic practitioner is crucial for a personalized plan.</p><table><tr><th>Category</th><th>Foods to Favor</th><th>Foods to Limit</th></tr><tr><td>Grains</td><td>Basmati rice, barley (moderation), quinoa (limited)</td><td>-</td></tr><tr><td>Vegetables</td><td>Leafy greens (spinach, kale), asparagus, cucumber, zucchini, broccoli (limited)</td><td>Spicy vegetables (peppers), dry & raw vegetables (cauliflower), sour vegetables (tomatoes)</td></tr><tr><td>Fruits</td><td>Sweet fruits (pears, apples, berries), pomegranate</td><td>Sweet & heavy fruits (bananas, mangoes), citrus fruits (lime, grapefruit)</td></tr><tr><td>Proteins</td><td>Lean proteins (chicken, fish, lentils, mung beans)</td><td>Red meat, processed meats, oily fish</td></tr><tr><td>Dairy</td><td>Sweet or buttermilk yogurt (limited), milk (moderation)</td><td>Cheese (aged), excessive cheese consumption</td></tr><tr><td>Nuts & Seeds</td><td>Almonds, pumpkin seeds, sunflower seeds (moderation)</td><td>Cashews, peanuts</td></tr><tr><td>Oils</td><td>Olive oil, limited ghee</td><td>Fried foods, vegetable oils (heavy processing)</td></tr><tr><td>Beverages</td><td>Cool water, coconut water, herbal teas (licorice, peppermint for Pitta, ginger for Vata)</td><td>Coffee, alcohol, sugary drinks</td></tr></table><p>Remember, this is a general guide. Consult an Ayurvedic practitioner for a personalized plan based on your specific needs.</p>"
                    con.markdown(html_string, unsafe_allow_html=True)
                elif(a_percent != b_percent and a_percent==c_percent):
                    con.subheader("It is likely for you to have both **Vata & Kapha** Dosha")
                    html_string  = "<h2>Vata-Kapha Balancing Diet: Finding Equilibrium</h2><p>Balancing Vata and Kapha doshas requires a diet that promotes lightness and reduces congestion. The following table provides a guideline for incorporating Vata-Kapha balancing foods into your diet. Remember, this is a general guide, and consulting an Ayurvedic practitioner is crucial for a personalized plan.</p><table><tr><th>Category</th><th>Foods to Favor</th><th>Foods to Limit</th></tr><tr><td>Grains</td><td>Lighter grains (quinoa, buckwheat, millet)</td><td>Heavy or processed grains (wheat, oats, rice)</td></tr><tr><td>Vegetables</td><td>Arugula, leafy greens (except collard greens), asparagus, celery, cruciferous vegetables (broccoli, cauliflower)</td><td>Sweet and starchy vegetables (potatoes, corn, peas), nightshade vegetables (tomatoes, eggplant)</td></tr><tr><td>Fruits</td><td>Pungent or tart fruits (apples, pears, cranberries, pomegranates)</td><td>Sweet and juicy fruits (bananas, mangoes, grapes, melons)</td></tr><tr><td>Proteins</td><td>Lean proteins (chicken, turkey, fish)</td><td>Fatty meats (red meat, lamb), dairy (except small amounts)</td></tr><tr><td>Spices</td><td>Warming spices (ginger, cumin, turmeric, black pepper)</td><td>Sweet and cooling spices (fennel, coriander, cardamom)</td></tr><tr><td>Oils</td><td>Mustard oil, sunflower oil, safflower oil</td><td>Ghee, coconut oil, heavy oils</td></tr><tr><td>Beverages</td><td>Warm water with lemon or ginger, herbal teas (especially ginger or dandelion)</td><td>Cold drinks, sugary drinks, dairy milk (except small amounts)</td></tr></table><p>Remember, this is a general guide. Consult an Ayurvedic practitioner for a personalized plan based on your specific needs.</p>"
                    con.markdown(html_string, unsafe_allow_html=True)
                elif(b_percent == c_percent and a_percent!=b_percent):
                    con.subheader("It is likely for you to have both **Pitta & Kapha** Dosha")
                    html_string  = "<h2>Pitta-Kapha Balancing Diet: Finding Moderation</h2><p>Balancing Pitta and Kapha doshas requires a diet that promotes digestion and avoids extremes. The following table provides a guideline for incorporating Pitta-Kapha balancing foods into your diet. Remember, this is a general guide, and consulting an Ayurvedic practitioner is crucial for a personalized plan.</p><table><tr><th>Category</th><th>Foods to Favor</th><th>Foods to Limit</th></tr><tr><td>Grains</td><td>Lighter grains (barley, millet, some buckwheat)</td><td>Heavy or processed grains (wheat, oats, excessive rice)</td></tr><tr><td>Vegetables</td><td>Leafy greens (except collard greens), asparagus, celery, some cruciferous vegetables (broccoli in moderation)</td><td>Sweet and starchy vegetables (potatoes, corn, peas), nightshade vegetables (tomatoes, eggplant)</td></tr><tr><td>Fruits</td><td>Sweet fruits with a mild cooling effect (pears, apples, berries)</td><td>Sweet and juicy fruits (bananas, mangoes, grapes, melons), sour fruits (citrus)</td></tr><tr><td>Proteins</td><td>Lean proteins (chicken, fish, lentils)</td><td>Fatty meats (red meat, lamb), excessive dairy</td></tr><tr><td>Spices</td><td>Warming spices with moderation (ginger, cumin, black pepper)</td><td>Sweet and cooling spices (fennel, coriander, cardamom in moderation)</td></tr><tr><td>Oils</td><td>Healthy fats like olive oil, limited ghee</td><td>Ghee (excess), coconut oil (excess), heavy oils</td></tr><tr><td>Beverages</td><td>Warm water with lemon or ginger, herbal teas (ginger, dandelion)</td><td>Cold drinks, sugary drinks, excessive dairy milk</td></tr</table><p>Remember, this is a general guide. Consult an Ayurvedic practitioner for a personalized plan based on your specific needs.</p>"
                    con.markdown(html_string, unsafe_allow_html=True)
                elif(b_percent == c_percent and a_percent==b_percent):
                    con.subheader("It is likely that you can have any of three Doshas which is not possible, please fill the information correctly!")