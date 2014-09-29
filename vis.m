T = dlmread('worlddata.csv',',',1,3);
D = T(:,1:end-4);
n = size(D,1);
d = size(D,2);
M = mean(D);
DN = (D-repmat(M,n,1))./(repmat(std(D),n,1));
[C,S,EV] = pca(DN);

%% +ve and -ve samples
V = [S(:,1) S(:,2) T(:,[11 12])];
X1 = V(V(:,3)==0,:);
X2 = V(V(:,3)==1,:);

%% plotting PCA
hold on;
plot(X1(:,1),X1(:,2),'*b');
plot(X2(:,1),X2(:,2),'*r');
plot([-5 10],[mean(V(:,2)) mean(V(:,2))],'--k');

%%
P = [S(T(:,11)==1,:) V(T(:,11)==1,4)];
ID = kmeans(P(:,1:end-1),3);

[ID P(:,end)]
