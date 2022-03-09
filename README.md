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
1) **(Done)** Nguyen, Bac; Morell, Carlos; De Baets, Bernard (2018). Scalable Large-Margin Distance Metric Learning Using Stochastic Gradient Descent. IEEE Transactions on Cybernetics, (), 1–12. doi:10.1109/TCYB.2018.2881417 
2) H. Ye, D. Zhan, N. Li and Y. Jiang, "Learning Multiple Local Metrics: Global Consideration Helps" in IEEE Transactions on Pattern Analysis & Machine Intelligence, vol. 42, no. 07, pp. 1698-1712, 2020. doi: 10.1109/TPAMI.2019.2901675 (пока нигде не нашел бесплатно, но abstract звучит интересно)
3) Bac Nguyen, Francesc J. Ferri, Carlos Morell, Bernard De Baets, An efficient method for clustered multi-metric learning, Information Sciences, Volume 471, 2019, Pages 149-163, ISSN 0020-0255, https://doi.org/10.1016/j.ins.2018.08.055.
4) **(Done)** B. Tang and H. He, "ENN: Extended Nearest Neighbor Method for Pattern Recognition [Research Frontier]," in IEEE Computational Intelligence Magazine, vol. 10, no. 3, pp. 52-60, Aug. 2015, doi: 10.1109/MCI.2015.2437512.
5) **(Done)** Bo Tang, Haibo He, Song Zhang, MCENN: A variant of extended nearest neighbor method for pattern recognition, Pattern Recognition Letters, Volume 133, 2020, Pages 116-122, ISSN 0167-8655, https://doi.org/10.1016/j.patrec.2020.01.015.
6) Chakraborty, Tapabrata (Rohan) et al. “Distance Metric Learned Collaborative Representation Classifier.” ArXiv abs/1905.01168 (2019): n. pag.
7) L. Feng, H. Wang, B. Jin, H. Li, M. Xue and L. Wang, "Learning a Distance Metric by Balancing KL-Divergence for Imbalanced Datasets," in IEEE Transactions on Systems, Man, and Cybernetics: Systems, vol. 49, no. 12, pp. 2384-2395, Dec. 2019, doi: 10.1109/TSMC.2018.2790914.
8) Chen S. et al. Curvilinear Distance Metric Learning // Advances in Neural Information Processing Systems. – 2019. – С. 4225-4234. http://papers.nips.cc/paper/8675-curvilinear-distance-metric-learning
9) [Metric Learning for Dynamic Text Classification](https://aclanthology.org/D19-6116) (Wohlwend et al., EMNLP 2019)
___

## 01.03.2022

Scalable Large-Margin Distance Metric Learning Using Stochastic Gradient Descent.

Основная идея та же, что у алгоритма LMNN (Large Margin Nearest Neighbors) &mdash; максимизировать некоторые отступы. В функцию потерь добавляют регуляризационное слагаемое trace(M) (ядерная норма M), которое штрафует за большой ранг матрицы M. Но основная часть статьи посвящена построению эффективного алгоритма для обучения с использованием SGD. С точки зрения точности представленная модель не может похвастаться значительным улучшением качества, однако достигнуто очень большое уменьшение времени обучения. Основная сложность оптимизации подобных функций потерь заключается в том, что на каждой итерации необходимо производить проекцию решения на множество положительно определенных матриц (PSD cone), для чего необходимо находить собственные значения матрицы. Для решения этой проблемы авторы на каждой итерации градиентного спуска делают шаг, который не выводит решение из множества положительно определенных матриц. Для этого были доказаны соответствующие теоремы.

___

## 06.03.2022

ENN: Extended Nearest Neighbor Method for Pattern Recognition

MCENN: A variant of extended nearest neighbor method for pattern
recognition

Две статьи, в первой из которых представлен новый метрический алгоритм, некоторое обобщение классического KNN. Это алгоритм в отличии от классического KNN при определении класса для нового объекта учитывает не только какие объекты являются его ближайшими соседями, но и для каких объектов обучающей выборки новый объект явдяется ближайшим соседом. Таким образом лучше учитывается распределение объектов и в некоторых случаях повышается качество предсказания. 

В второй статье предлагается метод для обучения расстояния, использование которого должно улучшить качество работы ENN. Как обычно обучается расстояние Махаланобиса, то есть линейное преобразование переводящее олбъекты в новое пространство. Использовался тот же подход, что и в методе NCA (Nearest Component Analysis): вводится вероятность правильной классификации каждого объекта обучающей выборки по остальной части и максимизируется количество верно классифицированных объектов, то есть напрямую оптимизируется LOO-ошибка. Как и для NCA, задача получается невыпуклая и возможно попадание в локальные минимумы при оптимизации градиентным спуском. Одним из недостатков NCA была высокая вероятность переобучения из-за прямой оптимизации LOO-ошибки, так что можно предположть такой же эффект и для MCENN алгоритма, но в статье данный вопрос не обсуждается.

___

## 09.03.2022

Learning a Distance Metric by Balancing KL-Divergence for Imbalanced Datasets

Статья поднимает проблему использования методов metric learning для несбалансированных данных. Авторы предоставляют новый метод metric learning, который способен учитывать дисбаланс классов и достигать лучшего качества чем друге методы на датасетах, в которых присутствует дисбаланс классов (оценивались accuracy, precision, recall, F-score). 
Вводится нормированная KL-дивергенция между различными классами после применения линейного преобразования (которое соответствует использованию новой метрики в исходном пространстве) после чего в качестве функционала качества используется геометрическое среднее этих KL-дивергенций для всех пар классов. Метод делает предположение, что каждый класс имеет нормальное распределение с некоторым матожиданием и ковариационной матрицей (могут быть различными для разных классов). Геометрическое среднее используется, для того чтобы метод старался одинаково хорошо "раздвигать" разные пары классов. Для лучшей дискриминативной способности добавляется слагаемое, штрафующее за расстояние между объектами разных классов. Это слагаемое берется с коэффициентом, который задает trade-off между геометрическим средним и максимизацией отступов. Также добавляются ограничения на матрицу задающую расстояние Махаланобиса: она должна быть положительно полуопределенной. Также ограничивается сумма расстояний между объектами одного класса. Обучение осуществляется с помощью градиентного спуска с проекциями на каждой итерации. То есть после каждого шага осуществляются проекции, для того чтобы текущее решение удовлетворяло ограничениям. На несбалансированных датасетах представленный метод показывает лучшие результаты чем LMNN, ITML и некоторые другие. В экспериментах использовался 1NN классификатор.

___

