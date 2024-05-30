########################  Single ROI #########################################################################################
import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\Users\LENOVO\truck\output_folder\frame_971.jpg')

# Resize the image to 640 by 480
image_resized = cv2.resize(image, (320, 240))

# Create a copy of the resized image for visualization
image_copy = image_resized.copy()

# Initialize the list to store the ROI points
roi_points = []

# Define the event callback
def select_roi(event, x, y, flags, param):
    global image_copy
    if event == cv2.EVENT_LBUTTONDOWN:
        roi_points.append((x, y))

        # Draw a circle where we clicked
        cv2.circle(image_copy, (x, y), 2, (0, 255, 0), 2)
        if len(roi_points) > 1:
            cv2.polylines(image_copy, [np.array(roi_points)], False, (0, 255, 0), 2)
        cv2.imshow('Image', image_copy)

    elif event == cv2.EVENT_RBUTTONDOWN:
        # Right click signals end of ROI selection process
        if len(roi_points) > 1:
            cv2.polylines(image_copy, [np.array(roi_points)], True, (0, 255, 0), 2)
        cv2.imshow('Image', image_copy)

# Set up the mouse callback
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', select_roi)

# Display the resized image and wait for a key press
cv2.imshow('Image', image_copy)
cv2.waitKey(0)

cv2.destroyAllWindows()
print(roi_points)





#################################   Multiple ROI ############################################################
# import cv2
# import numpy as np

# # Load the image
# image = cv2.imread(r'C:\Users\LENOVO\truck\output_folder\frame_3642.jpg')
# image_copy = image.copy()

# # Initialize the list to store the ROI points
# roi_points = []
# rois = []

# # Define the event callback
# def select_roi(event, x, y, flags, param):
#     global image_copy
#     if event == cv2.EVENT_LBUTTONDOWN:
#         roi_points.append((x, y))

#         # Draw a circle where we clicked
#         cv2.circle(image_copy, (x, y), 2, (0, 255, 0), 2)
#         if len(roi_points) > 1:
#             cv2.polylines(image_copy, [np.array(roi_points)], False, (0, 255, 0), 2)
#         cv2.imshow('Image', image_copy)

#     elif event == cv2.EVENT_RBUTTONDOWN:
#         # Right click signals end of ROI selection process
#         if len(roi_points) > 1:
#             cv2.polylines(image_copy, [np.array(roi_points)], True, (0, 255, 0), 2)
#             rois.append(list(roi_points))
#         roi_points.clear()
#         cv2.imshow('Image', image_copy)

# # Set up the mouse callback
# cv2.namedWindow('Image')
# cv2.setMouseCallback('Image', select_roi)

# # Display the image and wait for a key press
# cv2.imshow('Image', image)
# cv2.waitKey(0)

# cv2.destroyAllWindows()

# # Print the ROIs
# for i, roi in enumerate(rois):
#     print(f'ROI {i+1}: {roi}')










# import cv2
# import numpy as np

# # Load the image
# image_path = r'C:\Users\LENOVO\truck\output_folder\frame_980.jpg'
# image = cv2.imread(image_path)

# if image is not None:
#     image_copy = image.copy()

#     # Initialize the list to store the ROI points
#     roi_points = []

#     # Define the event callback
#     def select_roi(event, x, y, flags, param):
#         global image_copy
#         if event == cv2.EVENT_LBUTTONDOWN:
#             roi_points.append((x, y))

#             # Draw a circle where we clicked
#             cv2.circle(image_copy, (x, y), 2, (0, 255, 0), 2)
#             if len(roi_points) > 1:
#                 cv2.polylines(image_copy, [np.array(roi_points)], False, (0, 255, 0), 2)
#             cv2.imshow('Image', image_copy)

#         elif event == cv2.EVENT_RBUTTONDOWN:
#             # Right click signals end of ROI selection process
#             if len(roi_points) > 1:
#                 cv2.polylines(image_copy, [np.array(roi_points)], True, (0, 255, 0), 2)
#             cv2.imshow('Image', image_copy)

#     # Set up the mouse callback
#     cv2.namedWindow('Image')
#     cv2.setMouseCallback('Image', select_roi)

#     # Display the image and wait for a key press
#     cv2.imshow('Image', image)
#     cv2.waitKey(0)

#     cv2.destroyAllWindows()
#     print(roi_points)
# else:
#     print(f"Error: Unable to load the image from path: {image_path}")
