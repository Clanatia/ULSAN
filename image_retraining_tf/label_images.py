import tensorflow as tf
import socket
import sys

sys.stdin.encoding
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 13532))
server_socket.listen(1)
while 1:
    client_socket, address = server_socket.accept()
    print ("Client socker : ", address)
    f = open('C:/Users/Choi/Downloads/image_retraining/2.jpg', 'wb')
    image = client_socket.recv(1024)
    while 1:
        if image:
            f.write(image)
            image = client_socket.recv(1024)
        else:
            f.close();
            image_path = '2.jpg'
            break;
    client_socket.close()
    """image_path = sys.argv[1]"""
    # Read in the image_data
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line in tf.gfile.GFile("retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    
        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})
    
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (human_string, score))
        check = 0
        print('%s (score = %.5f)' % (human_string, score))
        if score >= 0.5:
            check = 1
            HOST = '10.0.1.122'
            PORT = 5008
            ADDR = (HOST, PORT)
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect(ADDR)
            if human_string == "adapter":
                s1 = u'어뎁터'
                #u1 = str(s1, "utf-8")
                clientSocket.send(s1.decode('cp949'))
            if human_string == "keyboard":
                s2= u'키보드'
                #u2 = str(s2, "utf-8")
                clientSocket.send(s2.decode('cp949'))
 
            clientSocket.close()
    if check == 0:
        HOST = '10.0.1.122'
        PORT = 5008
        ADDR = (HOST, PORT)
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect(ADDR)
        clientSocket.send(b'None')
        clientSocket.close()
server_socket.close()
