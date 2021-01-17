int maxArea(int* height, int heightSize) {
    int area, temp,high;
    area = 0;
    temp = 0;
    for(int i=0;i<heightSize;i++){
        for(int j=i;j<heightSize;j++){
            if (height[i]>height[j])
                high = height[j];
            else
                high = height[i];
            temp = (j-i)*high;
            if (temp>area)
                area = temp;
        }
    }
    return area;
}
