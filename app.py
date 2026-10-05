import streamlit as st
import pandas as pd
import plotly.express as px
from ai_engine import explain_product
from database import create_database, save_decision, get_decisions

# Create database
create_database()

# ======================================================
# PAGE SETTINGS
# ======================================================

st.set_page_config(
    page_title="AI Before-You-Buy",
    page_icon="🤖",
    layout="wide"
)


# ======================================================
# CUSTOM CSS
# ======================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.best-card {
    padding: 30px;
    border-radius: 20px;
    border: 2px solid rgba(128,128,128,0.3);
    text-align: center;
    margin: 25px 0;
}

.best-title {
    font-size: 22px;
    font-weight: 600;
}

.best-product {
    font-size: 36px;
    font-weight: 700;
    margin: 10px 0;
}

.best-score {
    font-size: 30px;
    font-weight: 600;
}

.best-price {
    font-size: 20px;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)


# ======================================================
# HEADER
# ======================================================

header_col1, header_col2 = st.columns([1, 4])

with header_col1:
    st.markdown(
        """
        <div style="
            text-align:center;
            font-size:80px;
            padding-top:10px;
        ">
            🤖
        </div>
        """,
        unsafe_allow_html=True
    )

with header_col2:
    st.markdown(
        """
        <div class="main-title">
            AI BEFORE-YOU-BUY
        </div>

        <div class="subtitle">
            Smart decisions. Better purchases.
        </div>

        <div style="
            text-align:center;
            font-size:16px;
            margin-bottom:25px;
        ">
            🤖 AI-powered • 🎯 Personalized • 📊 Explainable
        </div>
        """,
        unsafe_allow_html=True
    )


col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        "💰 **Budget Based**\n\n"
        "Find products within your budget."
    )

with col2:
    st.info(
        "🎯 **Personalized**\n\n"
        "Rank products using your priorities."
    )

with col3:
    st.info(
        "🤖 **AI Explained**\n\n"
        "Understand why a product was selected."
    )


# ======================================================
# LOAD PRODUCTS
# ======================================================

try:
    products = pd.read_csv("product.csv")

except FileNotFoundError:
    st.error(
        "product.csv was not found. "
        "Keep product.csv in the same folder as app.py."
    )
    st.stop()


# ======================================================
# USER REQUIREMENTS
# ======================================================

st.sidebar.header("🎯 Your Requirements")

# ======================================================
# PRODUCT CATEGORY
# ======================================================

categories = products["category"].unique().tolist()

selected_category = st.sidebar.selectbox(
    "🛍️ Product Category",
    categories
)


budget = st.sidebar.number_input(
    "💰 Maximum Budget (₹)",
    min_value=10000,
    max_value=200000,
    value=70000,
    step=5000
)


st.sidebar.subheader("Set Your Priorities")


st.sidebar.subheader("Set Your Priorities")


if selected_category == "Laptop":

    performance = st.sidebar.slider(
        "⚡ Performance",
        0,
        100,
        40
    )

    battery = st.sidebar.slider(
        "🔋 Battery",
        0,
        100,
        25
    )

    portability = st.sidebar.slider(
        "🎒 Portability",
        0,
        100,
        15
    )

    gaming = st.sidebar.slider(
        "🎮 Gaming",
        0,
        100,
        20
    )


elif selected_category == "Smartphone":

    performance = st.sidebar.slider(
        "⚡ Performance",
        0,
        100,
        30
    )

    battery = st.sidebar.slider(
        "🔋 Battery",
        0,
        100,
        30
    )

    portability = st.sidebar.slider(
        "📱 Portability",
        0,
        100,
        20
    )

    gaming = st.sidebar.slider(
        "🎮 Gaming",
        0,
        100,
        20
    )


# ======================================================
# FILTER BY BUDGET
# ======================================================

filtered_products = products[
    (products["category"] == selected_category)
    & (products["price"] <= budget)
].copy()

st.subheader("💻 Products Within Your Budget")


if filtered_products.empty:

    st.warning(
        "No laptops found within your budget. "
        "Try increasing your budget."
    )

    st.stop()


st.dataframe(
    filtered_products,
    width="stretch"
)


# ======================================================
# CALCULATE SCORE
# ======================================================

total_weight = (
    performance
    + battery
    + portability
    + gaming
)


if total_weight == 0:

    st.warning(
        "Please select at least one priority."
    )

    st.stop()


filtered_products["Score"] = (

    filtered_products["performance"] * performance

    + filtered_products["battery"] * battery

    + filtered_products["portability"] * portability

    + filtered_products["gaming"] * gaming

) / total_weight


# ======================================================
# RANK PRODUCTS
# ======================================================

ranked_products = filtered_products.sort_values(
    by="Score",
    ascending=False
).reset_index(drop=True)


st.subheader("🏆 Best Matches")


st.dataframe(
    ranked_products[
        [
            "name",
            "price",
            "performance",
            "battery",
            "portability",
            "gaming",
            "Score"
        ]
    ],
    width="stretch"
)


# ======================================================
# SCORE VISUALIZATION
# ======================================================

st.subheader(
    "📈 Product Score Visualization"
)


fig = px.bar(
    ranked_products,
    x="name",
    y="Score",
    title="Product Ranking Based on Your Priorities",
    labels={
        "name": "Product",
        "Score": "Decision Score"
    },
    range_y=[0, 100]
)


st.plotly_chart(
    fig,
    width="stretch"
)


# ======================================================
# BEST MATCH
# ======================================================

best = ranked_products.iloc[0]

# Save the recommendation to database
save_decision(
    product=best["name"],
    category=selected_category,
    price=best["price"],
    score=best["Score"],
    performance_weight=performance,
    battery_weight=battery,
    portability_weight=portability,
    gaming_weight=gaming
)


# ======================================================
# BEST MATCH
# ======================================================

best = ranked_products.iloc[0]

st.markdown(
    f"""
    <div class="best-card">
        <div class="best-title">
            🏆 YOUR BEST MATCH
        </div>

        <div class="best-product">
            {best['name']}
        </div>

        <div class="best-score">
            ⭐ {best['Score']:.2f} / 100
        </div>

        <div class="best-price">
            💰 ₹{best['price']:,}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ======================================================
# AI EXPLANATION
# ======================================================

st.subheader(
    "🧠 Why This Product?"
)


priorities = {

    "performance": performance,

    "battery": battery,

    "portability": portability,

    "gaming": gaming

}


with st.spinner(
    "🤖 AI is analyzing your choice..."
):

    try:

        ai_explanation = explain_product(
            best,
            budget,
            priorities
        )

        st.markdown(
            ai_explanation
        )

    except Exception as e:

        st.error(
            "Could not generate the AI explanation. "
            "Make sure Ollama is running and llama3.2 is installed."
        )

        st.code(str(e))


# ======================================================
# DECISION SCORE BREAKDOWN
# ======================================================

st.subheader(
    "📊 Decision Score Breakdown"
)


st.write(
    f"How {best['name']} achieved a score of "
    f"{best['Score']:.2f}/100"
)


performance_contribution = (
    best["performance"]
    * performance
    / total_weight
)


battery_contribution = (
    best["battery"]
    * battery
    / total_weight
)


portability_contribution = (
    best["portability"]
    * portability
    / total_weight
)


gaming_contribution = (
    best["gaming"]
    * gaming
    / total_weight
)


breakdown_data = pd.DataFrame({

    "Priority": [

        "Performance",

        "Battery",

        "Portability",

        "Gaming"

    ],

    "Contribution": [

        performance_contribution,

        battery_contribution,

        portability_contribution,

        gaming_contribution

    ]

})


st.dataframe(
    breakdown_data,
    width="stretch"
)


fig_breakdown = px.bar(

    breakdown_data,

    x="Priority",

    y="Contribution",

    title=(
        "How Each Priority Contributed "
        "to the Final Score"
    ),

    labels={
        "Contribution":
        "Score Contribution"
    }

)


st.plotly_chart(
    fig_breakdown,
    width="stretch"
)


# ======================================================
# WHY THIS PRODUCT OVER OTHERS
# ======================================================

st.subheader(
    "🤔 Why This Product Over Others?"
)


best_name = best["name"]


other_products = ranked_products[
    ranked_products["name"] != best_name
]


if not other_products.empty:

    for _, product in other_products.iterrows():

        st.write(
            f"### 🆚 {best_name} vs {product['name']}"
        )


        advantages = []

        disadvantages = []


        for feature in [

            "performance",

            "battery",

            "portability",

            "gaming"

        ]:

            best_score = best[feature]

            other_score = product[feature]


            if best_score > other_score:

                advantages.append(

                    f"{feature.title()} "
                    f"({best_score} vs {other_score})"

                )


            elif other_score > best_score:

                disadvantages.append(

                    f"{feature.title()} "
                    f"({best_score} vs {other_score})"

                )


        if advantages:

            st.write(

                "✅ **Why the best product wins:** "
                + ", ".join(advantages)

            )


        if disadvantages:

            st.write(

                "⚠️ **Where the other product is better:** "
                + ", ".join(disadvantages)

            )


        if not advantages and not disadvantages:

            st.write(
                "🤝 Both products have the same feature scores."
            )


        st.divider()


# ======================================================
# PRODUCT COMPARISON
# ======================================================

st.subheader(
    "📊 Compare Two Products"
)


product_names = products[
    products["category"] == selected_category
]["name"].tolist()


if len(product_names) >= 2:

    product1 = st.selectbox(

        "Select Product 1",

        product_names,

        index=0

    )


    product2 = st.selectbox(

        "Select Product 2",

        product_names,

        index=1

    )


    if product1 != product2:

        p1 = products[
            products["name"] == product1
        ].iloc[0]


        p2 = products[
            products["name"] == product2
        ].iloc[0]


        comparison_features = [

            "performance",

            "battery",

            "portability",

            "gaming",

            "display"

        ]


        # ==================================================
        # FEATURE COMPARISON
        # ==================================================

        comparison_data = []


        for feature in comparison_features:

            value1 = p1[feature]

            value2 = p2[feature]


            if value1 > value2:

                winner = product1

            elif value2 > value1:

                winner = product2

            else:

                winner = "Tie"


            comparison_data.append({

                "Feature":
                    feature.title(),

                product1:
                    value1,

                product2:
                    value2,

                "Winner":
                    winner

            })


        comparison = pd.DataFrame(
            comparison_data
        )


        st.write(
            "### 🔍 Feature-by-Feature Comparison"
        )


        st.dataframe(
            comparison,
            width="stretch"
        )


        # ==================================================
        # VISUAL COMPARISON
        # ==================================================

        chart_data = pd.DataFrame({

            "Feature":
                comparison_features,

            product1:
                [
                    p1[x]
                    for x in comparison_features
                ],

            product2:
                [
                    p2[x]
                    for x in comparison_features
                ]

        })


        chart_data = chart_data.melt(

            id_vars="Feature",

            var_name="Product",

            value_name="Score"

        )


        fig_compare = px.bar(

            chart_data,

            x="Feature",

            y="Score",

            color="Product",

            barmode="group",

            title="📈 Feature Comparison",

            range_y=[0, 100]

        )


        st.plotly_chart(

            fig_compare,

            width="stretch"

        )


        # ==================================================
        # PRICE COMPARISON
        # ==================================================

        st.write(
            "### 💰 Price Comparison"
        )


        col1, col2 = st.columns(2)


        with col1:

            st.metric(

                product1,

                f"₹{p1['price']:,}"

            )


        with col2:

            st.metric(

                product2,

                f"₹{p2['price']:,}"

            )


        # ==================================================
        # OVERALL WINNER
        # ==================================================

        score1 = sum(

            p1[x]

            for x in comparison_features

        )


        score2 = sum(

            p2[x]

            for x in comparison_features

        )


        st.write(
            "### 🏆 Overall Comparison"
        )


        if score1 > score2:

            st.success(

                f"🏆 {product1} wins this comparison "
                f"based on the selected features."

            )


        elif score2 > score1:

            st.success(

                f"🏆 {product2} wins this comparison "
                f"based on the selected features."

            )


        else:

            st.info(
                "🤝 Both products have the same overall score."
            )


    else:

        st.warning(
            "Please select two different products."
        )


else:

    st.warning(
        "At least two products are required for comparison."
    )


# ======================================================
# WHAT-IF ANALYSIS
# ======================================================

st.subheader(
    "🔄 What-If Analysis"
)


st.write(
    "Change your priorities and see "
    "how the recommendation changes."
)


whatif_performance = st.slider(

    "⚡ What-If Performance",

    0,

    100,

    performance,

    key="whatif_performance"

)


whatif_battery = st.slider(

    "🔋 What-If Battery",

    0,

    100,

    battery,

    key="whatif_battery"

)


whatif_portability = st.slider(

    "🎒 What-If Portability",

    0,

    100,

    portability,

    key="whatif_portability"

)


whatif_gaming = st.slider(

    "🎮 What-If Gaming",

    0,

    100,

    gaming,

    key="whatif_gaming"

)


whatif_total = (

    whatif_performance

    + whatif_battery

    + whatif_portability

    + whatif_gaming

)


if whatif_total > 0:

    whatif_products = products[
    (products["category"] == selected_category)
    & (products["price"] <= budget)
].copy()

    if not whatif_products.empty:

        whatif_products[
            "What-If Score"
        ] = (

            whatif_products["performance"]
            * whatif_performance

            + whatif_products["battery"]
            * whatif_battery

            + whatif_products["portability"]
            * whatif_portability

            + whatif_products["gaming"]
            * whatif_gaming

        ) / whatif_total


        whatif_products = (
            whatif_products
            .sort_values(
                by="What-If Score",
                ascending=False
            )
            .reset_index(drop=True)
        )


        whatif_best = (
            whatif_products.iloc[0]
        )


        st.success(

            f"🔄 With these new priorities, "
            f"the best match becomes "
            f"**{whatif_best['name']}** "
            f"with a score of "
            f"{whatif_best['What-If Score']:.2f}/100."

        )


    else:

        st.warning(
            "No products are available within "
            "the current budget."
        )


else:

    st.warning(
        "Please select at least one "
        "What-If priority."
    )



# ======================================================
# DECISION HISTORY
# ======================================================

st.subheader("🕘 Decision History")

decisions = get_decisions()

if decisions:
    history_data = pd.DataFrame(
        decisions,
        columns=[
            "Product",
            "Category",
            "Price",
            "Score",
            "Date & Time"
        ]
    )

    st.dataframe(
        history_data,
        width="stretch"
    )

else:
    st.info("No previous decisions yet.")