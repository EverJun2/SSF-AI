input_data=5 #�Է� �޴� ��
weight=3 #����ġ
target=8 #��ǥ�ϴ� ��
learning_rate=0.1 #�н� ��, ����ġ ����

pred=weight*input_data #����ġ*�Է� �޴� ��=������
error=pred-target #������-��ǥ�ϴ� ��=����
print("original error:", error)

slope=2*input_data*error #2*�Է� �޴� ��*����=�����Լ��� ����
print("slope:",slope)

new_weight=weight-learning_rate*slope #����ġ-�н� ��*����=���ο� ����ġ
print("new weight:",new_weight)

new_pred=new_weight*input_data #���ο� ����ġ*�Է� �޴� ��=���ο� ������
print("new prediction:", new_pred)

new_error=new_pred-target #���ο� ������-��ǥ �ϴ� ��=���ο� ����
print("new error:", new_error)