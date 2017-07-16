참조 블로그 : http://gusrb.tistory.com/16

# image_retraining_tf1.0 ver

final edit : 2017 5 4

git clone https://github.com/Clanatia/image_retraining_tf1.git



# 1) train 
    1) python retrain.py
    2) if error : python retrain.py --bottleneck_dir=bottlenecks --how_many_training_steps 500 --model_dir=inception \
    --output_graph=retrained_graph.pb --output_labels=retrained_labels.txt --image_dir=images --summaries_dir=log





bottleneck dir : 학습할 사진의 정보가 저장되는 경로

how many training steps : 학습 횟수

model_dir : 인터넷상에서 다운받는 모델링파일 경로

output graph : 그래프 파일 저장 경로와 이름

output labels : 학습된 데이터 이름 저장 텍스트 경로와 이름

image_dir : 학습할 이미지 폴더들 (각 폴더안에 이미지가 들어있다)

summaries_dir : 실질적 학습데이터 저장경로



# 2) Test cmd :

        python label_image.py IU.jpg
        python label_image.py SUJI.jpg



jupyter notebook :

        retrain.py -> retrain jupter notebook.ipynb
        label_image.py -> Test.ipynb
