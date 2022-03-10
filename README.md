# Дневник по научной работе у Дьяконова А.Г. (активный раздел)

Тема: Metric Learning
___

## 14.02.2022:

Начал со следующей обзорной статьи, после чего было решено сосредоточиться на классическом metric learning без использования нейросетей.
- [x] Mahmut Kaya H.s. Bilge «Deep Metric Learning: A Survey» // August 2019Symmetry 11(9):1066 DOI: 10.3390/sym11091066 https://www.researchgate.net/publication/335314481_Deep_Metric_Learning_A_Survey

Далее ознакомлюсь со следующим туториалом:
- [x] Suárez J. L., García S., Herrera F. A Tutorial on Distance Metric Learning: Mathematical Foundations, Algorithms, Experimental Analysis, Prospects and Challenges //arXiv preprint arXiv:1812.05944. – 2020. https://arxiv.org/abs/1812.05944

___

## 25.02.2022:

Закончил с туториалом, подробно разобрался с работой некоторых алгоритмов Metric Learning:

1) Алгоритмы понижения размерностей: PCA, LDA, ANMM
2) Алгоритмы для улучшения работы классификатора ближайших соседей: LMNN, NCA, NCMML и NCMC
3) Алгоритмы, основанные на теории информации: ITML, DMLMJ, MCML
4) Некоторые другоие методы Metric Learning: LSI (Learning with Side Information), DML-eig, LDML
5) Ядерные обобщения некоторых алгоритмов: KLMNN, KANMM, KDMLMJ, KDA

Список ниже будет дополняться статьями, которые я буду изучать:
- [x] Nguyen, Bac; Morell, Carlos; De Baets, Bernard (2018). Scalable Large-Margin Distance Metric Learning Using Stochastic Gradient Descent. IEEE Transactions on Cybernetics, (), 1–12. doi:10.1109/TCYB.2018.2881417 
- [ ] H. Ye, D. Zhan, N. Li and Y. Jiang, "Learning Multiple Local Metrics: Global Consideration Helps" in IEEE Transactions on Pattern Analysis & Machine Intelligence, vol. 42, no. 07, pp. 1698-1712, 2020. doi: 10.1109/TPAMI.2019.2901675 (пока нигде не нашел бесплатно, но abstract звучит интересно)
- [ ] Bac Nguyen, Francesc J. Ferri, Carlos Morell, Bernard De Baets, An efficient method for clustered multi-metric learning, Information Sciences, Volume 471, 2019, Pages 149-163, ISSN 0020-0255, https://doi.org/10.1016/j.ins.2018.08.055.
- [x] B. Tang and H. He, "ENN: Extended Nearest Neighbor Method for Pattern Recognition [Research Frontier]," in IEEE Computational Intelligence Magazine, vol. 10, no. 3, pp. 52-60, Aug. 2015, doi: 10.1109/MCI.2015.2437512.
- [x] Bo Tang, Haibo He, Song Zhang, MCENN: A variant of extended nearest neighbor method for pattern recognition, Pattern Recognition Letters, Volume 133, 2020, Pages 116-122, ISSN 0167-8655, https://doi.org/10.1016/j.patrec.2020.01.015.
- [x] Chakraborty, Tapabrata (Rohan) et al. “Distance Metric Learned Collaborative Representation Classifier.” ArXiv abs/1905.01168 (2019): n. pag.
- [x] L. Feng, H. Wang, B. Jin, H. Li, M. Xue and L. Wang, "Learning a Distance Metric by Balancing KL-Divergence for Imbalanced Datasets," in IEEE Transactions on Systems, Man, and Cybernetics: Systems, vol. 49, no. 12, pp. 2384-2395, Dec. 2019, doi: 10.1109/TSMC.2018.2790914.
- [ ] Chen S. et al. Curvilinear Distance Metric Learning // Advances in Neural Information Processing Systems. – 2019. – С. 4225-4234. http://papers.nips.cc/paper/8675-curvilinear-distance-metric-learning
- [ ] [Metric Learning for Dynamic Text Classification](https://aclanthology.org/D19-6116) (Wohlwend et al., EMNLP 2019)
- [ ] Huang, Zhiwu et al. “Cross Euclidean-to-Riemannian Metric Learning with Application to Face Recognition from Video.” IEEE Transactions on Pattern Analysis and Machine Intelligence 40 (2018): 2827-2840.
- [ ] Chen, Shuo et al. “Adversarial Metric Learning.” ArXiv abs/1802.03170 (2018): n. pag.
- [ ] Jie Xu, Lei Luo, Cheng Deng, and Heng Huang. Bilevel distance metric learning for robust image recognition. In NeurIPS, 2018. 1, 2.1
- [ ] Han-Jia Ye, De-Chuan Zhan, Xue-Min Si, Yuan Jiang, and Zhi-Hua Zhou. What makes objects similar: a unified multi-metric learning approach. In NeurIPS, 2016. 1, 2.1
- [ ] Pourya Zadeh, Reshad Hosseini, and Suvrit Sra. Geometric mean metric learning. In ICML, 2016. 1, 4.2
- [ ] Pengfei Zhu, Hao Cheng, Qinghua Hu, Qilong Wang, and Changqing Zhang. Towards generalized and efficient metric learning on riemannian manifold. In IJCAI, 2018. 1

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

## 10.03.2022

Distance Metric Learned Collaborative Representation Classifier

В статье рассказывается о том, как использоввание metric learning может улучшить работу CRC. Сперва опишу работу классического CRC. Предполагается, что имеется некоторая нейросеть, которая находит хорошее представление объекта, например с помощью сверточной нейронной сети получаем эмбеддинги картинок. В этом методе объект, который необходимо классифицировать, представляют в виде линейной комбинации всех объектов обучающей выборки, решая задачу линейной регрессии c регуляризацией. Далее для каждого из классов, представленных в выборке, считается некоторый функционал, который показывает насколько сильно при построении представления нового объекта в виде линейной комбинации всех объектов участвовали объекты каждого класса. Таким образом выбирается класс, который был важнее всех при конструировании представления объекта в виде линейной комбинации.

В классическом варианте при решении задачи линейной регрессии минимизируется квадрат l2-нормы с l2-регуляризацией. Авторы предлагают более общий подход: использовать метрику Махаланобиса, а также добавить в качестве дополнительного регуляризующего слагаемого спектральную норму матрицы обратной матрице из метрики Махаланобиса (если в метрике S^(-1), то в слагаемом спектральная норма S). В классической постановке получалась простая задача, для которой можно явно записать точное решение (хотя для его нахождения требуется обращать матрицу, размер которой растет с размером выборки). Для новой, получившейся задачи авторы представляют итерационный алгоритм, в котором поочередно оптимизируется матрица, задающая расстояние Махаланобиса и кодирующий вектор, задающий коэффициенты линейной комбинации объектов обучающей выборки.

Авторы показывали эффективность своей модели на 3 датасетах детализированных изображений с сетью VGG-19, предобученной на датасете ImageNet. Для сравнения использовались несколько других моделей, как использующих CRC подход, так и другие сети для классификации детализированных изображений. Эксперименты показали, что представленный подход, позволяет достигать заметно лучшего качества на всех 3 представленных датасетах.  

___ 

What makes objects similar: a unified multi-metric learning approach


___
