def floodFill(image, sr, sc, color, first=True, initialColor = 0):

    if first: 
        initialColor = image[sr][sc]
        first = False
    if initialColor == color: return image

    columns = len(image[0])-1
    rows = len(image)-1
    if sr < 0 or sc < 0 or sr > rows or sc > columns: return image

    if image[sr][sc] == initialColor: image[sr][sc] = color
    if sr + 1 <= rows and image[sr+1][sc] == initialColor: floodFill(image,sr+1,sc,color,first,initialColor)
    if sr - 1 >= 0 and image[sr-1][sc] == initialColor: floodFill(image,sr-1,sc,color,first,initialColor)
    if sc + 1 <= columns and image[sr][sc+1] == initialColor: floodFill(image,sr,sc+1,color,first,initialColor)
    if sc - 1 >= 0 and image[sr][sc-1] == initialColor: floodFill(image,sr,sc-1,color,first,initialColor)

    return image

print(floodFill([[0,0,0],
                [0,0,0],
                [0,0,0]],0,0,0))