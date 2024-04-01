def caculate_baking_time(mass, meatName):
    """
    Tính thời gian nướng thịt hợp lý cho một lò vi sóng tự động dựa trên loại thịt và khối lượng.

    Pramaters:
        meatName (string): Tên loại thịt, có hai loại là "Lợn" hoặc "Gà".
        mass (float): Khối lượng thịt cần nướng (kg).

    Returns:
        float: Thời giannướng thịt hợp lý (phút).

    Raises:
        ValueError: Nếu tên thịt không hợp lệ hoặc khối lượng thịt không nằm trong khoảng 0 < m <= 5.
        

    """
    
    # Kiểm tra tính hợp lệ của tên thịt
    if meatName not in ["Lợn", "Gà"]:
        raise ValueError("Loại thịt không hợp lên, loại thịt hợp lên là thịt lợn hoặc thịt gà.")
    
    # Kiểm tra tính hợp lệ của khối lượng
    if not 0 < mass <= 5:
        raise ValueError("Khối lượng không hợp lệ. Khối lượng phải nằm trong khoảng 0 < m <=5.")
    
    # Tính toán kết quả theo công thức
    if meatName == "Lợn":
        if mass < 2:
            return 10*mass
        else:
            return 10 + 5*mass
    elif meatName == "Gà":
        if mass < 2:
            return 8*mass
        else:
            return 8 +4*mass