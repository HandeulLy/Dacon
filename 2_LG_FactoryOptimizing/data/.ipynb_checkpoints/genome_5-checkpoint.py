# HDLY

import os
import pandas as pd
import numpy as np

from pathlib import Path
from data.simulator_5 import Simulator

simulator = Simulator()
submission_ini = pd.read_csv(os.path.join(Path(__file__).resolve().parent, 'sample_submission.csv'))
order_ini = pd.read_csv(os.path.join(Path(__file__).resolve().parent, 'order.csv'))

class Genome():
    def __init__(self, score_ini, input_len, output_len_1, output_len_2, h1=50, h2=50, h3=50):
        # 평가 점수 초기화
        self.score = score_ini
        
        # 히든레이어 노드 개수
        self.hidden_layer1 = h1
        self.hidden_layer2 = h2
        self.hidden_layer3 = h3
        
        ''' =================================================== '''
        
        # Event 신경망 가중치 생성
        '''
        # Event 신경망 가중치 생성
        self.w1 = np.random.randn(input_len, self.hidden_layer1)
        self.w2 = np.random.randn(self.hidden_layer1, self.hidden_layer2)
        self.w3 = np.random.randn(self.hidden_layer2, self.hidden_layer3)
        self.w4 = np.random.randn(self.hidden_layer3, output_len_1)
        
        # MOL 수량 신경망 가중치 생성
        self.w5 = np.random.randn(input_len, self.hidden_layer1)
        self.w6 = np.random.randn(self.hidden_layer1, self.hidden_layer2)
        self.w7 = np.random.randn(self.hidden_layer2, self.hidden_layer3)
        self.w8 = np.random.randn(self.hidden_layer3, output_len_2)
        '''
        # A
        self.w_a1 = np.random.randn(input_len, self.hidden_layer1)
        self.w_a2 = np.random.randn(self.hidden_layer1, self.hidden_layer2)
        self.w_a3 = np.random.randn(self.hidden_layer2, self.hidden_layer3)
        self.w_a4 = np.random.randn(self.hidden_layer3, output_len_1)
        # B
        self.w_b1 = np.random.randn(input_len, self.hidden_layer1)
        self.w_b2 = np.random.randn(self.hidden_layer1, self.hidden_layer2)
        self.w_b3 = np.random.randn(self.hidden_layer2, self.hidden_layer3)
        self.w_b4 = np.random.randn(self.hidden_layer3, output_len_1)
        
        # MOL 수량 신경망 가중치 생성
        # A
        self.w_a5 = np.random.randn(input_len, self.hidden_layer1)
        self.w_a6 = np.random.randn(self.hidden_layer1, self.hidden_layer2)
        self.w_a7 = np.random.randn(self.hidden_layer2, self.hidden_layer3)
        self.w_a8 = np.random.randn(self.hidden_layer3, output_len_2)
        # B
        self.w_b5 = np.random.randn(input_len, self.hidden_layer1)
        self.w_b6 = np.random.randn(self.hidden_layer1, self.hidden_layer2)
        self.w_b7 = np.random.randn(self.hidden_layer2, self.hidden_layer3)
        self.w_b8 = np.random.randn(self.hidden_layer3, output_len_2)
        
        
        ''' =================================================== '''
        
        # Event 종류
        '''
        self.mask = np.zeros([5], np.bool) # 가능한 이벤트 검사용 마스크
        '''
        self.event_map = {0:'CHECK_1', 1:'CHECK_2', 2:'CHECK_3', 3:'CHECK_4',
                          4:'PROCESS',
                          5:'CHANGE_12',6:'CHANGE_21',7:'CHANGE_34',8:'CHANGE_43'}
        
        # A
        self.mask_A = np.zeros([output_len_1], np.bool) # 가능한 이벤트 검사용 마스크
        #self.event_map_A = {0:'CHECK_1', 1:'CHECK_2', 2:'CHECK_3', 3:'CHECK_4', 4:'PROCESS'}
        # B 
        self.mask_B = np.zeros([output_len_1], np.bool) # 가능한 이벤트 검사용 마스크
        #self.event_map_B = {0:'CHECK_1', 1:'CHECK_2', 2:'CHECK_3', 3:'CHECK_4', 4:'PROCESS'}
        
        ''' =================================================== '''
        
        # 변수 초기화
        '''
        self.check_time = 28    # 28시간 검사를 완료했는지 검사, CHECK Event시 -1, processtime_time >=98 이면 28
        self.process = 0        # 생산 가능 여부, 0 이면 28 시간 검사 필요
        self.process_mode = 0   # 생산 물품 번호 1~4, stop시 0
        self.process_time = 0   # 생산시간이 얼마나 지속되었는지 검사, PROCESS +1, CHANGE +1, 최대 140
        '''
        # A
        self.check_time_A = 28
        self.process_A = 0
        self.process_mode_A = 0
        self.process_time_A = 0
        self.change_time_A = 6
        self.change_mode_A = 5
        self.check_A=''
        self.check_ok_A = False
        
        # B
        self.check_time_B = 28 
        self.process_B = 0     
        self.process_mode_B = 0
        self.process_time_B = 0
        self.change_time_B = 6
        self.change_mode_B = 5
        self.check_B=''
        self.check_ok_B = False
    
    ###########################################
    ''' UPDATE MASK'''
    '''
    def update_mask(self):
        self.mask[:] = False
        if self.process == 0:
            if self.check_time == 28:
                self.mask[:4] = True
            if self.check_time < 28:
                self.mask[self.process_mode] = True
        if self.process == 1:
            self.mask[4] = True
            if self.process_time > 98:
                self.mask[:4] = True
    '''
    def update_mask_A(self):
        self.mask_A[:] = False
        
        if self.process_A == 0 and self.check_ok_A == False :
            if self.check_time_A == 28:
                self.mask_A[:4] = True
            if self.check_time_A < 28:
                self.mask_A[self.process_mode_A] = True
        elif self.process_A == 0 and self.check_ok_A:
            self.check_A = self.check_Aid
            if self.check_A[-1] is '1':
                if self.change_time_A ==6:
                    self.mask_A[5] = True
                if self.change_time_A < 6:
                    self.mask_A[self.change_mode_A] = True                    
            elif self.check_A[-1] is '2':
                if self.change_time_A ==6:
                    self.mask_A[6] = True  
                if self.change_time_A < 6:
                    self.mask_A[self.change_mode_A] = True                      
            elif self.check_A[-1] is '3':
                if self.change_time_A ==6:
                    self.mask_A[7] = True  
                if self.change_time_A < 6:
                    self.mask_A[self.change_mode_A] = True                      
            elif self.check_A[-1] is '4':
                if self.change_time_A ==6:
                    self.mask_A[8] = True                     
                if self.change_time_A < 6:
                    self.mask_A[self.change_mode_A] = True  
                    
        if self.process_A == 1:
            self.mask_A[4] = True
            if self.process_time_A > 98:
                self.mask_A[:4] = True
                
    def update_mask_B(self):
        self.mask_B[:] = False
        
        if self.process_B == 0 and self.check_ok_B == False :
            if self.check_time_B == 28:
                self.mask_B[:4] = True
            if self.check_time_B < 28:
                self.mask_B[self.process_mode_B] = True
        elif self.process_B == 0 and self.check_ok_B:
            self.check_B = self.check_Bid
            if self.check_B[-1] is '1':
                if self.change_time_B ==6:
                    self.mask_B[5] = True
                if self.change_time_B < 6:
                    self.mask_B[self.change_mode_B] = True                    
            elif self.check_B[-1] is '2':
                if self.change_time_B ==6:
                    self.mask_B[6] = True  
                if self.change_time_B < 6:
                    self.mask_B[self.change_mode_B] = True                      
            elif self.check_B[-1] is '3':
                if self.change_time_B ==6:
                    self.mask_B[7] = True  
                if self.change_time_B < 6:
                    self.mask_B[self.change_mode_B] = True                      
            elif self.check_B[-1] is '4':
                if self.change_time_B ==6:
                    self.mask_B[8] = True                     
                if self.change_time_B < 6:
                    self.mask_B[self.change_mode_B] = True 
                    
        if self.process_B == 1:
            self.mask_B[4] = True
            if self.process_time_B > 98:
                self.mask_B[:4] = True
                
    ###########################################
    
    def forward(self, inputs):
        # Event 신경망
        '''
        net = np.matmul(inputs, self.w1)
        net = self.linear(net)
        net = np.matmul(net, self.w2)
        net = self.linear(net)
        net = np.matmul(net, self.w3)
        net = self.sigmoid(net)
        net = np.matmul(net, self.w4)
        net = self.softmax(net)
        net += 1
        net = net * self.mask
        out1 = self.event_map[np.argmax(net)]
        '''
        # A
        net = np.matmul(inputs, self.w_a1)
        net = self.linear(net)
        net = np.matmul(net, self.w_a2)
        net = self.linear(net)
        net = np.matmul(net, self.w_a3)
        net = self.sigmoid(net)
        net = np.matmul(net, self.w_a4)
        net = self.softmax(net)
        net += 1
        net = net * self.mask_A
        out1_a = self.event_map[np.argmax(net)]
        # B
        net = np.matmul(inputs, self.w_b1)
        net = self.linear(net)
        net = np.matmul(net, self.w_b2)
        net = self.linear(net)
        net = np.matmul(net, self.w_b3)
        net = self.sigmoid(net)
        net = np.matmul(net, self.w_b4)
        net = self.softmax(net)
        net += 1
        net = net * self.mask_B
        out1_b = self.event_map[np.argmax(net)]
        
        # MOL 수량 신경망
        '''
        net = np.matmul(inputs, self.w5)
        net = self.linear(net)
        net = np.matmul(net, self.w6)
        net = self.linear(net)
        net = np.matmul(net, self.w7)
        net = self.sigmoid(net)
        net = np.matmul(net, self.w8)
        net = self.softmax(net)
        out2 = np.argmax(net)
        out2 /= 2    
        '''
        # A
        net = np.matmul(inputs, self.w_a5)
        net = self.linear(net)
        net = np.matmul(net, self.w_a6)
        net = self.linear(net)
        net = np.matmul(net, self.w_a7)
        net = self.sigmoid(net)
        net = np.matmul(net, self.w_a8)
        net = self.softmax(net)
        out2_a = np.argmax(net)
        out2_a *= 5.8579
        # B 
        net = np.matmul(inputs, self.w_b5)
        net = self.linear(net)
        net = np.matmul(net, self.w_b6)
        net = self.linear(net)
        net = np.matmul(net, self.w_b7)
        net = self.sigmoid(net)
        net = np.matmul(net, self.w_b8)
        net = self.softmax(net)
        out2_b = np.argmax(net)
        out2_b *= 5.8579        
        
        # return out1, out2
        return out1_a, out2_a, out1_b, out2_b
        
    
    ###########################################

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        return np.exp(x) / np.sum(np.exp(x), axis=0)
    
    def linear(self, x):
        # return x
        return x / np.max(x)
    
    def leakyReLU(self, x):
        return np.maximum(0.01*x, x)
    
    ###########################################
    
    def create_order(self, order):
        for i in range(30):
            order.loc[91+i,:] = ['0000-00-00', 0, 0, 0, 0]   
            
        return order
    
    ###########################################
    
    def predict(self, order):
        order = self.create_order(order)
        self.submission = submission_ini
        self.submission.loc[:, 'PRT_1':'PRT_4'] = 0
        self.check_Aid=''
        self.check_Bid=''
        
        change_time, change_point = 0, 0
        stop_time, stop_point = 0, 0
        
        for s in range(self.submission.shape[0]):
            self.update_mask_A()
            self.update_mask_B()
            
            inputs = np.array(order.loc[s//24:(s//24+30), 'BLK_1':'BLK_4']).reshape(-1)
            inputs = np.append(inputs, s%24)
            
            # out1, out2 = self.forward(inputs)
            out1_a, out2_a, out1_b, out2_b = self.forward(inputs)
            
            # Check the Process Mode
            '''
            if out1 == 'CHECK_1':
                if self.process == 1:
                    self.process = 0
                    self.check_time = 28
                self.check_time -= 1
                self.process_mode = 0
                if self.check_time == 0:
                    self.process = 1
                    self.process_time = 0
            elif out1 == 'CHECK_2':
                if self.process == 1:
                    self.process = 0
                    self.check_time = 28
                self.check_time -= 1
                self.process_mode = 1
                if self.check_time == 0:
                    self.process =1
                    self.process_time = 0
            elif out1 == 'CHECK_3':
                if self.process == 1:
                    self.process = 0
                    self.check_time = 28
                self.check_time -= 1
                self.process_mode = 2
                if self.check_time == 0:
                    self.process = 1
                    self.process_time = 0
            elif out1 == 'CHECK_4':
                if self.process == 1:
                    self.process = 0
                    self.check_time = 28
                self.check_time -= 1
                self.process_mode = 3
                if self.check_time == 0:
                    self.process = 1
                    self.process_time = 0
            elif out1 == 'PROCESS':
                self.process_time += 1
                if self.process_time == 140:
                    self.process = 0
                    self.check_time = 28
            '''
            
            '''
            if out1_a == 'CHECK_1':
                if self.process_A == 1:
                    self.process_A = 0
                    self.check_time_A = 28
                self.check_time_A -= 1
                self.process_mode_A = 0
                if self.check_time_A == 0:
                    self.process_A = 1
                    self.process_time_A = 0
            elif out1_a == 'CHECK_2':
                if self.process_A == 1:
                    self.process_A = 0
                    self.check_time_A = 28
                self.check_time_A -= 1
                self.process_mode_A = 1
                if self.check_time_A == 0:
                    self.process_A =1
                    self.process_time_A = 0
            elif out1_a == 'CHECK_3':
                if self.process_A == 1:
                    self.process_A = 0
                    self.check_time_A = 28
                self.check_time_A -= 1
                self.process_mode_A = 2
                if self.check_time_A == 0:
                    self.process_A = 1
                    self.process_time_A = 0
            elif out1_a == 'CHECK_4':
                if self.process_A == 1:
                    self.process_A = 0
                    self.check_time_A = 28
                self.check_time_A -= 1
                self.process_mode_A = 3
                if self.check_time_A == 0:
                    self.process_A = 1
                    self.process_time_A = 0
            elif out1_a == 'PROCESS':
                self.process_time_A += 1
                if self.process_time_A == 140:
                    self.process_A = 0
                    self.check_time_A = 28
            
            if out1_b == 'CHECK_1':
                if self.process_B == 1:
                    self.process_B = 0
                    self.check_time_B = 28
                self.check_time_B -= 1
                self.process_mode_B = 0
                if self.check_time_B == 0:
                    self.process_B = 1
                    self.process_time_B = 0
            elif out1_b == 'CHECK_2':
                if self.process_B == 1:
                    self.process_B = 0
                    self.check_time_B = 28
                self.check_time_B -= 1
                self.process_mode_B = 1
                if self.check_time_B == 0:
                    self.process_B =1
                    self.process_time_B = 0
            elif out1_b == 'CHECK_3':
                if self.process_B == 1:
                    self.process_B = 0
                    self.check_time_B = 28
                self.check_time_B -= 1
                self.process_mode_B = 2
                if self.check_time_B == 0:
                    self.process_B = 1
                    self.process_time_B = 0
            elif out1_b == 'CHECK_4':
                if self.process_B == 1:
                    self.process_B = 0
                    self.check_time_B = 28
                self.check_time_B -= 1
                self.process_mode_B = 3
                if self.check_time_B == 0:
                    self.process_B = 1
                    self.process_time_B = 0
            elif out1_b == 'PROCESS':
                self.process_time_B += 1
                if self.process_time_B == 140:
                    self.process_B = 0
                    self.check_time_B = 28
            '''
            
            # A
            if 'CHECK' in out1_a :
                if out1_a[-1] == '1':
                    if self.process_A == 1:
                        self.process_A = 0
                        self.check_time_A = 28
                    self.check_time_A -= 1
                    self.process_mode_A = 0
                    self.check_Aid=out1_a[-1]               
                    if self.check_time_A == 0:
                        self.process_A = 1
                        self.process_time_A = 0
                elif out1_a[-1] == '2':
                    if self.process_A == 1:
                        self.process_A = 0
                        self.check_time_A = 28
                    self.check_time_A -= 1
                    self.process_mode_A = 1
                    self.check_Aid=out1_a[-1]                
                    if self.check_time_A == 0:
                        self.process_A =1
                        self.process_time_A = 0
                elif out1_a[-1] == '3':
                    if self.process_A == 1:
                        self.process_A = 0
                        self.check_time_A = 28
                    self.check_time_A -= 1
                    self.process_mode_A = 2
                    self.check_Aid=out1_a[-1]                
                    if self.check_time_A == 0:
                        self.process_A = 1
                        self.process_time_A = 0
                elif out1_a[-1] == '4':
                    if self.process_A == 1:
                        self.process_A = 0
                        self.check_time_A = 28
                    self.check_time_A -= 1
                    self.process_mode_A = 3
                    self.check_Aid=out1_a[-1]                
                    if self.check_time_A == 0:
                        self.process_A = 1
                        self.process_time_A = 0
                else : pass
            elif out1_a == 'PROCESS':
                self.process_time_A += 1
                if self.process_time_A == 140:
                    self.process_A = 0
                    self.check_time_A = 28
            elif 'CHANGE' in out1_a :
                if self.process_A == 1:
                    self.process_A = 0
                    self.change_time_A = 6
                self.process_time_A += 1
                if self.process_time_A == 140:
                    self.process_A = 1
                    self.process_time_A = 0           
                self.change_time_A -= 1
                self.check_Aid=out1_a[-1]
                if self.change_time_A == 0:
                    self.process_A =1
                    self.process_time_A = 0
                    self.change_time_A = 6
                if out1_a == 'CHANGE_12': self.change_mode_A = 5
                if out1_a == 'CHANGE_21': self.change_mode_A = 6
                if out1_a == 'CHANGE_34': self.change_mode_A = 7
                if out1_a == 'CHANGE_43': self.change_mode_A = 8

            # B
            if 'CHECK' in out1_b :
                if out1_b[-1] == '1':
                    if self.process_B == 1:
                        self.process_B = 0
                        self.check_time_B = 28
                    self.check_time_B -= 1
                    self.process_mode_B = 0
                    self.check_Bid=out1_b[-1]               
                    if self.check_time_B == 0:
                        self.process_B = 1
                        self.process_time_B = 0
                elif out1_b[-1] == '2':
                    if self.process_B == 1:
                        self.process_B = 0
                        self.check_time_B = 28
                    self.check_time_B -= 1
                    self.process_mode_B = 1
                    self.check_Bid=out1_b[-1]                
                    if self.check_time_B == 0:
                        self.process_B =1
                        self.process_time_B = 0
                elif out1_b[-1] == '3':
                    if self.process_B == 1:
                        self.process_B = 0
                        self.check_time_B = 28
                    self.check_time_B -= 1
                    self.process_mode_B = 2
                    self.check_Bid=out1_b[-1]                
                    if self.check_time_B == 0:
                        self.process_B = 1
                        self.process_time_B = 0
                elif out1_b[-1] == '4':
                    if self.process_B == 1:
                        self.process_B = 0
                        self.check_time_B = 28
                    self.check_time_B -= 1
                    self.process_mode_B = 3
                    self.check_Bid=out1_b[-1]                
                    if self.check_time_B == 0:
                        self.process_B = 1
                        self.process_time_B = 0
                else : pass
            elif out1_b == 'PROCESS':
                self.process_time_B += 1
                if self.process_time_B == 140:
                    self.process_B = 0
                    self.check_time_B = 28
            elif 'CHANGE' in out1_b :
                if self.process_B == 1:
                    self.process_B = 0
                    self.change_time_B = 6
                self.process_time_B += 1
                if self.process_time_B == 140:
                    self.process_B = 1
                    self.process_time_B = 0           
                self.change_time_B -= 1
                self.check_Bid=out1_b[-1]
                if self.change_time_B == 0:
                    self.process_B =1
                    self.process_time_B = 0
                    self.change_time_B = 6
                if out1_b == 'CHANGE_12': self.change_mode_B = 5
                if out1_b == 'CHANGE_21': self.change_mode_B = 6
                if out1_b == 'CHANGE_34': self.change_mode_B = 7
                if out1_b == 'CHANGE_43': self.change_mode_B = 8
                                
                    
            # Submission MODE
            '''
            self.submission.loc[s, 'Event_A'] = out1
            if self.submission.loc[s, 'Event_A'] == 'PROCESS':
                self.submission.loc[s, 'MOL_A'] = out2
            else:
                self.submission.loc[s, 'MOL_A'] = 0
            '''
            # A
            self.submission.loc[s, 'Event_A'] = out1_a
            if self.submission.loc[s, 'Event_A'] == 'PROCESS':
                #self.submission.loc[s, 'MOL_A'] = out2_a
                     self.submission.loc[s, 'MOL_A'] = 0
                elif 24*15 <= s < 24*30:
                     self.submission.loc[s, 'MOL_A'] = out2_a * (140.5907407/24)
                elif 24*30 <= s < 24*61:
                     self.submission.loc[s, 'MOL_A'] = out2_a * (140.8055556/24)
                else:
                     self.submission.loc[s, 'MOL_A'] = out2_a * (141.0185185/24)

            else:
                self.submission.loc[s, 'MOL_A'] = 0                
            # B
            self.submission.loc[s, 'Event_B'] = out1_b
            if self.submission.loc[s, 'Event_B'] == 'PROCESS':
                #self.submission.loc[s, 'MOL_B'] = out2_b
                if s < 24*15:
                     self.submission.loc[s, 'MOL_B'] = 0
                elif 24*15 <= s < 24*30:
                     self.submission.loc[s, 'MOL_B'] = out2_b * (140.5907407/24)
                elif 24*30 <= s < 24*61:
                     self.submission.loc[s, 'MOL_B'] = out2_b * (140.8055556/24)
                else:
                     self.submission.loc[s, 'MOL_B'] = out2_b * (141.0185185/24)

            else:
                self.submission.loc[s, 'MOL_B'] = 0
                
            
        # 23일간 MOL = 0
        # 최초 재고량으로 처리할 수 있으니까, 여기를 조금 손 봐야한다
        '''
        # option 1
        self.submission.loc[:24*23, 'MOL_A'] = 0
        self.submission.loc[:24*23, 'MOL_B'] = 0
        '''
        
        ''' 
        # option 2        
        self.submission.loc[:24*14, 'MOL_A'] = 0
        self.submission.loc[:24*14, 'MOL_B'] = 0
        
        for i in range(24*14, 24*23):
            if self.submission.loc[i,'Event_A'] == 'CHECK_2':
                break
            elif :
                self.submission.loc[i,'MOL_A'] = 0
                
        for j in range(24*14, 24*23):
            if self.submission.loc[j,'Event_B'] == 'CHECK_2':
                break
            elif :
                self.submission.loc[i,'MOL_B'] = 0
        '''
        
        # case 3
#         '''
        # 14일간 MOL = 0
        self.submission.loc[:24*14, 'MOL_A'] = 0
        self.submission.loc[:24*14, 'MOL_B'] = 0
        
        self.check_point = 0
        for i in range(24*14,24*23):
            if self.submission.loc[i,'Event_A'] == 'CHECK_2':
                self.check_point = 1
            elif self.submission.loc[i,'Event_A'] == 'PROCESS' and self.check_point == 1:
                continue
            
            elif self.submission.loc[i,'Event_A'] == 'CHECK_1' or self.submission.loc[i,'Event_A'] == 'CHECK_3' or self.submission.loc[i,'Event_A'] == 'CHECK_4' :
                self.check_point = 0
                self.submission.loc[i,'MOL_A'] = 0
                
            else :
                self.submission.loc[i,'MOL_A'] = 0
        
        self.check_point = 0        
        for j in range(24*14,24*23):
            if self.submission.loc[j,'Event_B'] == 'CHECK_2':
                self.check_point = 1
            elif self.submission.loc[j,'Event_B'] == 'PROCESS' and self.check_point == 1:
                continue
            
            elif self.submission.loc[j,'Event_B'] == 'CHECK_1' or self.submission.loc[i,'Event_B'] == 'CHECK_3' or self.submission.loc[i,'Event_B'] == 'CHECK_4' :
                self.check_point = 0
                self.submission.loc[j,'MOL_B'] = 0
                
            else :
                self.submission.loc[j,'MOL_B'] = 0
#         '''
        
        ########################################
        
        # A 라인 = B 라인
        # self.submission.loc[:, 'Event_B'] = self.submission.loc[:, 'Event_A']
        # self.submission.loc[:, 'MOL_B'] = self.submission.loc[:, 'MOL_A']
        
        # 변수 초기화
        '''
        self.check_time = 28
        self.process = 0
        self.process_mode = 0
        self.process_time = 0
        '''
        # A
        self.check_time_A = 28
        self.process_A = 0
        self.process_mode_A = 0
        self.process_time_A = 0
        self.change_time_A = 6
        self.change_mode_A = 5
        # B
        self.check_time_B = 28
        self.process_B = 0
        self.process_mode_B = 0
        self.process_time_B = 0
        self.change_time_B = 6
        self.change_mode_B = 5
        
        return self.submission    
    
def genome_score(genome):
    submission = genome.predict(order_ini)    
    genome.submission = submission    
    genome.score, _ = simulator.get_score(submission)    
    return genome