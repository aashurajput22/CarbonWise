from app import validate_inputs, calculate_emissions, get_category, generate_recommendations

def test_valid_inputs():
    valid, error = validate_inputs(10, 100, 2, 1)
    assert valid == True

def test_negative_inputs():
    valid, error = validate_inputs(-1, 100, 2, 1)
    assert valid == False

def test_emission_calculation():
    result = calculate_emissions(10, "Bike", 100, "Vegetarian", "Medium", 2, "Medium", 1)
    assert result["Net Total"] >= 0

def test_category():
    category, badge = get_category(100)
    assert "Low" in category

def test_recommendations():
    tips = generate_recommendations("Bike", 120, "Vegetarian", "Medium", 2, "Medium")
    assert len(tips) == 6
