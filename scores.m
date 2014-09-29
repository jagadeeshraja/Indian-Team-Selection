%% not out counter index
O = dlmread('worlddatabowling.csv',','1,2);
XN = (O-repmat(mean(O),size(O,1),1))./(repmat(std(O),size(O,1),1));

F1 = XN(:,3)+XN(:,6)+XN(:,7);
F1 = F1./XN(:,end-3);
F1(:,1) = F1(:,1)+XN(:,5);

F1 = [F1 O(:,end)]; %adding player indices
F1(:,3) = O(:,8);
csvwrite('notout_counter.csv',F1);

%% scorability counter index

F2 = XN(:,4)+XN(:,end-4);
F2 = [F2 O(:,end)];
F2(:,3) = O(:,8);
csvwrite('scorability_counter.csv',F2);
