# import cv2
# import streamlit as st
# import numpy as np
#
# st.title("Image Histogram Equalization")
#
# uploaded_image = st.file_uploader("Select an image", type=["jpg", "jpeg", "png"])
#
# if uploaded_image is not None:
#
#     image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)
#
#     if image is not None:
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         img_equal_hist = cv2.equalizeHist(gray_image)
#
#         img_equal_hist_orig = cv2.equalizeHist(gray_image)
#
#         col1, col2, col3 = st.columns(3)
#         col1.image(image, caption="Original Image", use_column_width=True)
#         col2.image(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB), caption="Grayscale Image", use_column_width=True)
#         col3.image(cv2.cvtColor(img_equal_hist_orig, cv2.COLOR_BGR2RGB), caption="Image After Histogram Equalization", use_column_width=True)
#
#         st.write("Original Histogram Equalization")
#         st.line_chart(np.histogram(gray_image, bins=256, range=(0, 256))[0])
#
#         st.write("Image After Histogram Equalization")
#         st.line_chart(np.histogram(img_equal_hist, bins=256, range=(0, 256))[0])
#     else:
#         st.write("Unable read image")

# import cv2
# import numpy as np
# import streamlit as st
#
# def adaptive_histogram_equalization(input_image, clip_limit=2.0, grid_size=(8, 8)):
#     clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=grid_size)
#     adaptive_output = clahe.apply(input_image)
#     return adaptive_output
#
# st.title("Image Histogram Equalization")
#
# uploaded_image = st.file_uploader("Select an image", type=["jpg", "jpeg", "png"])
#
# if uploaded_image is not None:
#     image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)
#
#     if image is not None:
#         gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         adaptive_output = adaptive_histogram_equalization(gray_image)
#
#         col1, col2, col3 = st.columns(3)
#         col1.image(image, caption="Original Image", use_column_width=True)
#         col2.image(gray_image, caption="Grayscale Image", use_column_width=True)
#         col3.image(cv2.cvtColor(adaptive_output, cv2.COLOR_BGR2RGB), caption="Adaptive Histogram Equalization", use_column_width=True)
#
#         hist_orig, bins = np.histogram(gray_image.ravel(), bins=256, range=(0, 256))
#         hist_adaptive, _ = np.histogram(adaptive_output.ravel(), bins=256, range=(0, 256))
#
#         st.write("Histograms of the image:")
#         st.line_chart(hist_orig)
#         st.line_chart(hist_adaptive)
#     else:
#         st.write("Unable read image")

# ==========================READ IMAGE=============================
# import cv2
# import numpy as np
# import streamlit as st
#
# def adaptive_histogram_equalization(input_image, clip_limit=2.0, grid_size=(8, 8)):
#     clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=grid_size)
#     adaptive_output = clahe.apply(input_image)
#     return adaptive_output
#
# st.title("Image Histogram Equalization")
#
# image_path = "1.jpg"
#
# image = cv2.imread(image_path)
#
# if image is not None:
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     adaptive_output = adaptive_histogram_equalization(gray_image)
#
#     col1, col3 = st.columns(2)
#     col1.image(image, caption="Original Image", use_column_width=True)
#     col3.image(cv2.cvtColor(adaptive_output, cv2.COLOR_BGR2RGB), caption="Adaptive Histogram Equalization", use_column_width=True)
#
#     hist_orig, bins = np.histogram(gray_image.ravel(), bins=256, range=(0, 256))
#     hist_adaptive, _ = np.histogram(adaptive_output.ravel(), bins=256, range=(0, 256))
#
#     st.write("Histograms of the image:")
#     st.line_chart(hist_orig)
#     st.line_chart(hist_adaptive)
# else:
#     st.write(f"Image file '{image_path}' does not exist.")

