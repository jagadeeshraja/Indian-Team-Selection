%% INDIAN Bowlers

% notout counter %%%%%%%
D1 = dlmread('indiabowling.csv',',',1,2);

XN = (D1-repmat(mean(D1),size(D1,1),1))./(repmat(std(D1),size(D1,1),1));

F1 = XN(:,5)+XN(:,9)+XN(:,10);
F1 = F1./XN(:,2);
F1(:,1) = F1(:,1)+XN(:,8);

F1 = [F1 D1(:,end)]; %adding player indices
F1S = sortrows(F1,-1);
%csvwrite('india_notout_counter.csv',F1);

% scorability counter %%%%%%
F2 = XN(:,6)+XN(:,end-1);
F2(:,end+1) = D1(:,end);
F2S = sortrows(F2,1);
%csvwrite('india_scorability_counter.csv',F2);


%% INDIAN Batsmen

% endurance %%%%%%%%
D1 = dlmread('indiabatting.csv',',',1,2);

XN = (D1-repmat(mean(D1),size(D1,1),1))./(repmat(std(D1),size(D1,1),1));

F1 = XN(:,3)./XN(:,2);

F1 = [F1 D1(:,end)]; %adding player indices
F1S = sortrows(F1,-1);
%csvwrite('india_endurance.csv',F1S);

% scorability %%%%%%%
F2 = XN(:,4)./XN(:,2);
F2(:,end+1) = D1(:,end);
F2S = sortrows(F2,-1);
%csvwrite('india_scorability.csv',F2S);

