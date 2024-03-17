def check_uet_success(score, specialized):
    """
    Kiểm tra kết quả đỗ đại học của thí sinh dựa trên điểm thi và ngành học mong muốn.

    Pramaters:
        score (float): Điểm thi của thí sinh.
        specialized (string): Ngành học sinh viên muốn ứng tuyển.

    Returns:
        str: Kết quả có đỗ chuyên ngành đó không ("Đỗ" hoặc "Trượt").

    Raises:
        ValueError: Nếu ngành học không hợp lệ hoặc điểm thi không nằm trong khoảng từ 0 đến 30.

    """
    
    # Kiểm tra tính hợp lệ của ngành
    if specialized not in ["CNTT", "CKT"]:
        raise ValueError("Chuyên ngành không hợp lệ, chuyên ngành hợp lệ là CNTT hoặc CKT.")
    
    # Kiểm tra tính hợp lệ của điểm thi
    if not 0 <= score <= 30:
        raise ValueError("Điểm thi không hợp lệ. Điểm thi phải nằm trong khoảng từ 0 đến 30.")
    
    # Kiểm tra ngành học và điểm thi để xác nhận kết quả
    if specialized == "CKT" and score >=25:
        return "Đỗ"
    elif specialized == "CNTT" and score >= 27:
        return "Đỗ"
    else:
        return "Trượt"