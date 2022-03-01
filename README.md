# Дневник по научной работе у Дьяконова А.Г. (активный раздел)

Тема: Metric Learning
___

## 14.02.2022:

Начал со следующей обзорной статьи, после чего было решено сосредоточиться на классическом metric learning без использования нейросетей.
- [ ] Mahmut Kaya H.s. Bilge «Deep Metric Learning: A Survey» // August 2019Symmetry 11(9):1066 DOI: 10.3390/sym11091066 https://www.researchgate.net/publication/335314481_Deep_Metric_Learning_A_Survey

Далее ознакомлюсь со следующим туториалом:
- [ ] Suárez J. L., García S., Herrera F. A Tutorial on Distance Metric Learning: Mathematical Foundations, Algorithms, Experimental Analysis, Prospects and Challenges //arXiv preprint arXiv:1812.05944. – 2020. https://arxiv.org/abs/1812.05944

___

## 25.02.2022:

Закончил с туториалом, подробно разобрался с работой некоторых алгоритмов Metric Learning:

1) Алгоритмы понижения размерностей: PCA, LDA, ANMM
2) Алгоритмы для улучшения работы классификатора ближайших соседей: LMNN, NCA, NCMML и NCMC
3) Алгоритмы, основанные на теории информации: ITML, DMLMJ, MCML
4) Некоторые другоие методы Metric Learning: LSI (Learning with Side Information), DML-eig, LDML
5) Ядерные обобщения некоторых алгоритмов: KLMNN, KANMM, KDMLMJ, KDA

Список ниже будет дополняться статьями, которые я буду изучать:
1) Nguyen, Bac; Morell, Carlos; De Baets, Bernard (2018). Scalable Large-Margin Distance Metric Learning Using Stochastic Gradient Descent. IEEE Transactions on Cybernetics, (), 1–12. doi:10.1109/TCYB.2018.2881417 

___

## 01.03.2022

Scalable Large-Margin Distance Metric Learning Using Stochastic Gradient Descent.

Основная идея та же, что у алгоритма LMNN (Large Margin Nearest Neighbors) &mdash; максимизировать некоторые отступы. В функцию потерь добавляют регуляризационное слагаемое trace(M) (ядерная норма M), которое штрафует за большой ранг матрицы M. Но основная часть статьи посвящена построению эффективного алгоритма для обучения с использованием SGD. С точки зрения точности представленная модель не может похвастаться значительным улучшением качества, однако достигнуто очень большое уменьшение времени обучения. Основная сложность оптимизации подобных функций потерь заключается в том, что на каждой итерации необходимо производить проекцию решения на множество положительно определенных матриц (PSD cone), для чего необходимо находить собственные значения матрицы. Для решения этой проблемы авторы на каждой итерации градиентного спуска делают шаг, который не выводит решение из множества положительно определенных матриц. Для этого были доказаны соответствующие теоремы.

___


