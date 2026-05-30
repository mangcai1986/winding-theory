# Contribution to the winding theory -Introduction of a unified method for the treatment of winding topology

Von der Fakultät für Elektrotechnik, Informationstechnik, Physik der Technischen Universität Carolo-Wilhelmina zu Braunschweig 

zur Erlangung des Grades eines Doktors 

der Ingenieurwissenschaften (Dr.-Ing.) 

genehmigte Dissertation 

von Mang Cai 

aus Chenghai, China 

eingereicht am: 23.11.2016 

mündliche Prüfung am: 14.02.2017 

1. Referent: Prof. Dr.-Ing. W.-R. Canders 

2. Referent: Prof. Dr.-Ing. habil. Dr. h. c. K. Hameyer 

Druckjahr: 2017 

Dissertation an der Technischen Universität Braunschweig, Fakultät für Elektrotechnik, Informationstechnik, Physik 

To Xiaoxi. 

# Acknowledgments

This work was done during my career as a scientic research assistant at Institute for Electrical Machines, Traction and Drives (IMAB), TU-Braunschweig from 2011 to 2016. 

First of all, I wish to express my sincere gratitude to my doctoral advisor, Prof. Dr.-Ing. Wolf-Rüdiger Canders who accompany me from beginning to end during my time in IMAB. Indeed, this work is inspired by his expertise competence and research passion. The comprehensive and valuable discussion about electrical machines, about politics, culture, morality, and humanity in the eastern and western will benet me for life. My particular thanks go to Prof. Dr.-Ing. Markus Henke, Director of IMAB for giving me the chance to work as a scientic research assistant and accepting the role as head of the examination committee. Without his permanent support, this work cannot be nished so quickly. My foremost thanks also go to Prof. Dr.-Ing. habil. Dr. h. c. Kay Hameyer, Head of the Institute of Electrical machines (IEM) at RWTH Aachen University for giving me the chance to present my work in IEM and accepting to be a member of the examining board of this thesis. 

I thank Prof. Dr.-Ing. Johannes Zentner for introducing me to the world of electrical machines and Dr.-Ing. Helmut Mosebach for his kind encouragement and expertise discussion. I thank Dr.-Ing. Günter Tareilus for the support during my preparation for the teaching and especially for the doctoral examination. Credit goes to Dr. -Ing. Ahamed Bilal Asaf Ali for extensive proofreading of the manuscript and correcting the English grammar in great detail. 

I would like to warmly acknowledge all the colleagues at IMAB. In particular, I thank my oce colleague M. Sc. Christian Heister for the expertise discussion, for the discussion about family, life, sport, and coffee. I thank M. Sc. Henning Schillingmann for the German abstract correction and Herbert Rawe for the support during my doctoral examination preparation. In addition, I thank the Secretaries Ms. Barbara Tiedge and Dorothee Ottow for their support. 

Finally, I am grateful to my parents for their understanding and support. My deep in heart thanks go to my wife Xiaoxi Li who shared my daily life during the realization of this thesis and my son Boyong Cai who made this period so enriching for me. 

Regensburg, June 2017 

Mang Cai 

# Abstract

The main contribution of this work to the winding theory of electrical machines is the introduction of a unied method for the analysis and design of winding topology, which occurs through a straightforward procedure. To better explain the new idea, four dierent languages are used to describe the proposed method during this work. They are the mathematical formulation of the method through the introduced matrix notation, the graphical presentation of the method through the introduced illustrations, the implementation of the method through the high-level computer language Python and the natural human language in English. 

Before this is done, a comprehensive introduction of the winding in electrical machines in respect of the theoretical and practical aspects is given, underlying the importance of the winding topology in the electromagnetic energy conversion process (chapter 1) and its impacts on the machine performance (chapter 2). 

After that, a comprehensive introduction to the eld of winding topology is given, which is separated into two parts. 

The rst part (chapter 3) serves as to make a clear understanding of the investigated topic, which includes the denition of the winding topology, the terminology used in this thesis and the denition of the problems to be treated. This part is nished by a historical review of the research activities. The second part (chapter 4) gives a classication of the methods for winding topology treatment in a more systematical way than that provided in the classic textbook from H. Sequenz. Moreover, newly proposed methods are included in the introduced framework, so that an overall overview of the so far achieved methods is obtained. 

The introduction of the method and its application are given in chapter 5 and 6 respectively. 

The introduction of the method (chapter 5) begins with the denition of the assumptions. On that basis, the derivation of the analytical formula for the calculation of the winding factor of an arbitrary harmonic order is given, which is formulated later by using matrix notation and presented by using graphical form. A unied method implemented in Python for analysis of winding topology is then given. In the rest of this chapter, the theoretical background of the unied method for design of winding topology is step by step explained. A comprehensive Python code for the implementation of each step as well as for the illustration of the results is also given. 

Application of the proposed method for winding topology design (chapter 6) is given through 3 reasonably chosen examples. They are 3-phase winding of 12 slots with fundamental and 5-th over-harmonic as working harmonic, 3-phase winding of 9 slots with 4-th over-harmonic as working harmonic and 6-phase winding of 24 slots with 5-th over-harmonic as working harmonic. All the design results are compared with that of various publications, obtained by various authors by using dierent methods, which shows the validity and generality of the proposed method. 

An outlook about the recent development as well as the development tendency in the eld of winding of electrical machines is given in the last chapter (chapter 7) of this thesis. Some potential research topics are given, leading the thesis to the end. 

# Kurzfassung

Der Hauptbeitrag der vorliegenden Arbeit zur Wicklungstheorie der elektrischen Maschinen liegt darin, dass eine einheitliche und deterministische Methode für die Analyse und das Design der Wicklungstopologien eingeführt wird. Um diese neue Idee verständlicher zu erklären, werden vier unterschiedlichen Sprachen benutzt. Dazu zählt die mathematische Formulierung der Methode durch Anwendung der Matrizennotation, die graphische Darstellung der Methode durch neu eingeführte graphische Objekte, die Implementierung der Methode durch die höhere Programmiersprache Python und die Ausformulierung der Methode in englischer Sprache. 

Bevor die Methode vorgestellt wird, wird eine umfangreiche Einführung zur Wicklung der elektrischen Maschinen bezüglich der theoretischen und praktischen Aspekte gegeben. Damit werden die Wichtigkeit der Wicklung bei der elektromechanischen Energieumformung (Kapitel 1) und deren Einuss auf die Maschinenperformance (Kapitel 2) herausgehoben. 

Danach folgt eine umfangreiche Einführung in das Gebiet der Wicklungstopologie, welche in zwei Kapitel (Kapitel 3 und 4) aufgeteilt ist. 

Der erste Teil (Kapitel 3) dient dazu, dem Leser ein klares Verständnis für das untersuchte Gebiet zu geben. Dies beinhaltet die Denition des Begris Wicklungstopologie, die Terminologie, die in der Arbeit angewendet wird und die Denition des zu behandelnden Problems. Ein historischer Rückblick der Forschungsaktivitäten in diesem Gebiet schlieÿt diesen Teil ab. Der zweite Teil (Kapitel 4) gibt eine Klassikation der Methoden zur Behandlung der Wicklungstopologien in systematischerer Weise, als die gegebene im klassischen Buch von H. Sequenz. Auÿerdem werden neue publizierte Ansätze in die eingeführte Klassikation eingebettet, so dass ein Überblick der bisher bekannten Methoden geliefert wird. 

Die Vorstellung der Methode und ihre Anwendung sind jeweils in Kapitel 5 und 6 gegeben. 

Die Vorstellung der Methode (Kapitel 5) fängt mit der Denition der Annahmen an. Darauf basierend ist die Herleitung der analytischen Formel zur Berechnung des Wicklungsfaktors einer beliebigen harmonischen 

Ordnung gegeben. Diese Formel wird später durch Einführung der Matrizennotation erweitert, so dass gleichzeitig die Wicklungsfaktoren verschiedener harmonischer Ordnungen berechnet werden können. Die Ergebnisse werden durch Einführung von graphischen Objekten visualisiert. Danach wird eine einheitliche und deterministische Methode für die Analyse der Wicklungstopologien gegeben, welche in Python implementiert wird. Weiterhin werden in diesem Kapitel die theoretischen Grundlagen der einheitlichen Methode für das Design der Wicklungstopologien erkl-ärt. Ein umfangreiches Python-Programm für die Implementierung der Methode und die Visualisierung der Designergebnisse wird vorgestellt. Anschlieÿend (Kapitel 6) werden drei mit angemessener Sorgfalt ausgewählte Beispiele vorgestellt, welche die Anwendung der Methode für das Design der Wicklungstopologien zeigt. Diese sind das Design einer 3- phasigen Wicklung mit 12 Nuten und der Grundharmonischen, bzw. der 5. Harmonischen als Arbeitswelle, das Design einer 3-phasigen Wicklung mit 9 Nuten und der 4. Harmonischen als Arbeitswelle, sowie das Design einer 6-phasigen Wicklung mit 24 Nuten und der 5. Harmonischen als Arbeitswelle. Alle Ergebnisse werden mit denen aus Veröentlichungen verglichen, die durch unterschiedliche Autoren und mit verschiedenen Methoden erzielt wurden. Dies bestätigt die Allgemeingültigkeit der Methode. 

Abschlieÿend werden im letzten Kapitel die derzeitigen Entwicklungen und die Entwicklungstendenzen in diesem Gebiet vorgestellt und die daraus folgenden potentiellen Forschungsthemen beleuchtet. 

# Contents

# 1. The double roles of the winding in the electromechanical energy conversion 1

1.1. The lumped quantity approach . . . 1 

1.1.1. Separation of the electrical energy variation into dissipative and coupling electrical energy variation 3 

1.1.2. The relationship between the coupling electrical energy variation, the mechanical energy variation and the magnetic energy variation . . 4 

1.1.3. The relationship between the coupling electrical energy variation, the mechanical energy variation and the magnetic co-energy variation 5 

1.2. The eld quantity approach . . . 5 

1.3. Winding: a double-way bridge 7 

# 2. The impacts of the winding on the machine performance 10

2.1. The winding insulation . . . 10 

2.2. The number of turns . . 10 

2.3. The winding production method . . 11 

2.4. The winding topology . . . 15 

2.4.1. Torque quality . . . 15 

2.4.2. Torque-speed operation range . . . . 16 

2.4.3. Inductance 17 

2.4.4. Electromagnetic losses . . 17 

2.4.4.1. Winding copper losses . . . 17 

2.4.4.2. Iron losses 18 

2.4.4.3. Permanent magnet eddy current losses . 21 

# 3. An introduction to the winding topology 23

3.1. The understanding of the winding topology . . . . . . . . 23 

3.1.1. The geometrical point of view . . . . 23 

3.1.2. The electromagnetic point of view . . . 23 

3.2. A short introduction to the terminology . . . . 24 

3.2.1. The existing terminology for the description of winding topology . . 24 

3.2.2. Terminology used in this thesis for the description of winding topology . . . 26 

3.3. The two main problems for winding topology treatment . 27 

3.3.1. Winding topology analysis . . . . . 27 

3.3.2. Winding topology design . . . 27 

3.4. A historical review of the research activities . . . . . 28 

3.4.1. Treatment of fundamental harmonic winding topology till the 1950s 28 

3.4.1.1. The great success in the achievement of winding topology treatment methods . . 29 

3.4.1.2. The research limitation . . 31 

3.4.2. The treatment of over-harmonic winding topology since the 1980s . 31 

3.4.2.1. The adaptation of the long standing methods for over-harmonic winding topology 33 

3.4.2.2. The research limitations . . . . 34 

# 4. A systematical classication of winding topology treatment methods 35

4.1. Preamble 35 

4.2. Winding topology analysis methods . . . 38 

4.2.1. Methods based on EMF analysis . . . 40 

4.2.1.1. The composite Approach . . . . . . . . . 40 

4.2.1.2. The de-composite approach . . . . . 42 

4.2.2. Methods based on MMF analysis . . . . 49 

4.2.2.1. Analysis of the MMF function of dierent domain . 50 

4.2.2.2. Analysis of the MMF function of dierent shape . . 51 

4.3. Winding topology design methods . . . 55 

4.3.1. Winding topology layout methods . . . . . . 55 

4.3.1.1. The deterministic approach . . . . . 55 

4.3.1.2. The stochastic approach . . . . 68 

4.3.2. Winding topology modication methods . . . . . . 70 

4.3.2.1. The multi-layer approach . . . . . . . . . 71 

4.3.2.2. The multi-slot approach . . . . . . . 71 

4.3.2.3. The multi-turn approach . . . . . . . . . 71 

4.3.2.4. The multi-conductor approach . . . . . . 72 

4.3.2.5. The multi-coil approach . . . . . . . 73 

# 5. A unied method for the treatment of the winding topology 79

5.1. Assumptions 79 

5.2. The theoretical and mathematical Basis . . 80 

5.2.1. Derivation of the analytical formula for the calculation of winding factor of arbitrary space harmonic order . . 80 

5.2.2. Calculation of the winding factor space harmonic spectrum using matrix notation . . 84 

5.2.3. The unique mapping of the winding factor harmonic spectrum and the normalized MMF distribution 85 

5.2.4. The graphical presentation of the matrix notation 86 

5.2.4.1. The winding factor harmonic spectrum . 86 

5.2.4.2. The normalized MMF distribution . . . . 87 

5.2.4.3. The symmetrical multi-phase current system . . 89 

5.2.4.4. The winding direction . . . 90 

5.2.4.5. The normalized conductor distribution matrix: topology of the multi-phase winding 92 

5.3. A unied method for winding topology analysis . . . . . . 94 

5.3.1. The analysis procedures . . . 94 

5.3.2. Implementation of the method in Python . . . . . 94 

5.4. A unied method for winding topology design . . . . . . . 95 

5.4.1. The ideal winding factor harmonic spectrum . . . 95 

5.4.2. The ideal normalized MMF distribution . . . . . . 96 

5.4.3. The symmetrical multi-phase current system . . . 97 

5.4.3.1. Number of phases equal number of slots . 97 

5.4.3.2. Number of phases equal half number of slots . . 98 

5.4.3.3. The other cases . . 98 

5.4.4. Topology of the normalized conductor distribution matrix: types of winding topology . 99 

5.4.5. Determination of the normalized conductor distribution matrix: the primitive double-layer multiphase winding . . 102 

5.4.6. Exploitation of the symmetrical properties of the primitive multi-phase winding . . . 104 

5.4.6.1. Rotational symmetry: the symmetry between the primitive phase windings . . . 105 

5.4.6.2. Mirror symmetry: the symmetry within the primitive phase winding . . . . . . . . 106 

5.4.7. Connection of the conductors of the primitive coil group: the primitive coils . . 108 

5.4.7.1. The double-way connection approach . . 109 

5.4.7.2. The single-way connection approach . . . 110 

5.4.8. Derivation of the winding topology . . . . . . . . . 112 

5.4.8.1. Design of the multi-turn winding topology 112 

5.4.8.2. Design of the multi-layer winding topology 113 

5.4.8.3. Design of the multi-coil winding topology 114 

5.4.8.4. Design of the multi-conductor winding topology . . . . . 114 

5.4.8.5. Design of the double-layer winding topology116 

5.4.8.6. Design of the single-layer winding topology117 

5.4.9. Evaluation of the winding topology: calculation of the winding factor harmonic spectrum . . . . . . . 119 

6. Application of the proposed method for the treatment of winding topology 125 

6.1. The 3-phase fundamental and over-harmonic winding of 12 slots . . . 126 

6.1.1. The design procedure 126 

6.1.1.1. The ideal winding factor harmonic spectrum126 

6.1.1.2. The ideal normalized MMF distribution . 126 

6.1.1.3. The normalized conductor distribution matrix and the primitive double-layer multiphase winding . . 128 

6.1.1.4. The rotational symmetry and the primitive single-phase winding . . . . . . . . . 133 

6.1.1.5. The mirror symmetry and the primitive coil group . . . 136 

6.1.1.6. The connection matrix and the primitive coils . 139 

6.1.1.7. Derivation of the multi-turn and the multilayer winding topology 142 

6.1.1.8. Derivation of the multi-coil and the multiconductor winding topology . . . . . . . . 145 

6.1.1.9. Derivation of the double-layer winding topology . . . 148 

6.1.1.10. Derivation of the single-layer winding topology . . . . . . 151 

6.1.2. Evaluation and discussion of the results . . . . . . 154 

6.1.2.1. The fundamental harmonic winding . . . 154 

6.1.2.2. The over-harmonic winding . . . . . . . . 160 

6.2. The 3-phase winding of 9 slots with working Harmonic of 4 167 

6.2.1. The normalized conductor distribution matrix and the primitive double layer winding . . . . . . . . 168 

6.2.2. The primitive single phase winding and the primitive coil group . . 169 

6.2.3. The double- and single-way connections . . . . . . 170 

6.2.4. Discussion of the resulting winding topologies . . . 173 

6.2.4.1. The multi-turn and multi-layer winding topology . . 173 

6.2.4.2. The single- and double-layer winding topology . . . . . 176 

6.2.4.3. The multi-coil and multi-conductor winding topology . . . 176 

6.3. The 6-phase winding of 24 slots with working harmonic of 5179 

7. Winding theory: a far from completed topic 186 

7.1. Electric winding topology reconguration . . . . . 187 

7.1.1. Asynchronous machine . . . 187 

7.1.2. Synchronous machine 188 

7.2. Winding with individual slot excitation 188 

7.3. Issues of further investigation . . . 190 

A. Implementation of the proposed method in Python 192 

A.1. Codes for the winding topology analysis . . . . . . . . . 192 

A.2. Codes for the graphical presentation . . 193 

A.2.1. The winding factor harmonic spectrum . . . . . . 193 

A.2.2. The normalized MMF distribution . . . . . . 194 

A.2.3. The normalized conductor distribution matrix . . . 194 

A.2.4. The winding topology . . . 196 

A.3. Codes of the design algorithm . . . 198 

A.3.1. Obtain the ideal MMF distribution from the ideal winding factor harmonic spectrum . 198 

A.3.2. Obtain the primitive multi-phase winding topology from the ideal MMF distribution and the multiphase current system . . 199 

# Contents

A.3.3. Obtain the primitive single-phase winding topology through detecting the rotation symmetry . . . . . 200 

A.3.4. Obtain the primitive coil group through detecting the mirror symmetry . . 201 

A.3.5. Obtain the primitive coils through detecting the connection matrix 202 

A.3.6. Obtain the coils of particular winding topology . . 206 

# Bibliography 209

# Nomenclature 219

# List of Figures 227

# 1. The double roles of the winding in the electromechanical energy conversion

From the energy point of view, an electrical machine can be seen as an electromechanical energy converter. With the aid of the magnetic energy $E _ { m }$ , it changes the electrical energy $E _ { e }$ into mechanical energy $E _ { \Omega }$ and vice versa, where the process is followed by the generation of the dissipative energy $E _ { d }$ (heat energy). 

The energy conservation law ensures that, for each innite small time interval dt, for the motor mode, there is: 

$$
\mathrm{d} E _ {e} = \mathrm{d} E _ {\Omega} + \mathrm{d} E _ {m} + \mathrm{d} E _ {d} \tag {1.1}
$$

while for the generator mode, there is: 

$$
\mathrm{d} E _ {\Omega} = \mathrm{d} E _ {e} + \mathrm{d} E _ {m} + \mathrm{d} E _ {d} \tag {1.2}
$$

This phenomenon can be illustrated through Figure 1.1. 

Since it is an electromechanical process, to describe the process completely, electrical and mechanical state variables are needed. Dierent choices of the electrical and mechanical state variables are possible with various abstractive level. For the following discussion, a multi-phase electrical machine specic and practical approach is chosen. 

There are two dierent ways to describe the energy conversion process: lumped quantity approach and eld quantity approach. The lumped quantities are understood as, the determination of such quantities happens only at dened location, while for the eld quantities, the determination of such quantities (if possible) occurs through the whole space. 

The following discussion is specic to the case of motor mode (equation 1.1) but can be extended for the generator mode without diculty. 

# 1.1. The lumped quantity approach

For the lumped quantity approach, the m-phase current is chosen as the electrical state variables, which is considered as an algebraic vector i with each phase current as its element. The rotor angular position is chosen as the mechanical state variable. To include the case of multiple rotors, just like magnetic gear [3] or electrical transmission system [4], the mechanical state variable is also represented with an algebraic vector Ω, with the angular position of each rotor as its element. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/31e61314fcabb61620384312c0cc0eb8448f3f67c7e45ddce24ef1905904360d.jpg)



Figure 1.1.: The electrical machine as an electromechanical energy converter


According to the classical electromagnetic theory [82], the energy variation can be predicted through the following equations respective. 

# 1.1.1. Separation of the electrical energy variation into dissipative and coupling electrical energy variation

For the electrical energy variation, there is: 

$$
\mathrm{d} E _ {e} = \boldsymbol {i} ^ {\mathrm{T}} \boldsymbol {u} \mathrm{d} t \tag {1.3}
$$

where the elements of u and i are the instantaneous phase voltage and current of the m-phase winding. For a detailed analysis of the process, it is to separate the phase voltage into two parts, with the rst part caused due to electrical resistance of the winding R and the second part due to the change of the magnetic ux linkage acting on the winding ψ: 

$$
\boldsymbol {u} = \mathbf {R} \boldsymbol {i} + \frac {\mathrm{d} \boldsymbol {\psi}}{\mathrm{d} t} \tag {1.4}
$$

Equation 1.3 can then be formulated as: 

$$
\mathrm{d} E _ {e} = \mathbf {R} | \boldsymbol {i} | ^ {2} \mathrm{d} t + \boldsymbol {i} ^ {\mathrm{T}} \mathrm{d} \psi = \mathrm{d} E _ {e, d} + \mathrm{d} E _ {e, c} \tag {1.5}
$$

with the rst term of the dissipative electrical energy d $E _ { e , d }$ and the second term the coupling electrical energy d $E _ { e , c }$ . 

A better understanding of the conversion process can be obtained, if the coupling electrical energy is further separated into two parts, which is mathematically to formulate the absolute dierential part dψ as a sum of several partial dierential parts by using the state variables: 

$$
\mathrm{d} \boldsymbol {\psi} = \mathbf {J} _ {\Omega} \mathrm{d} \boldsymbol {\Omega} + \mathbf {J} _ {i} \mathrm{d} \boldsymbol {i} \tag {1.6}
$$

with the Jacobian matrix: 

$$
\mathrm{J} _ {\Omega , n k} = \frac {\partial \psi_ {n}}{\partial \Omega_ {k}} \tag {1.7}
$$

$$
\mathrm{J} _ {i, n k} = \frac {\partial \psi_ {n}}{\partial i _ {k}}
$$

The coupling electrical energy d $E _ { e , c }$ can then be formulated as: 

$$
\mathrm{d} E _ {e, c} = \boldsymbol {i} ^ {\mathrm{T}} \mathbf {J} _ {\Omega} \mathrm{d} \boldsymbol {\Omega} + \boldsymbol {i} ^ {\mathrm{T}} \mathbf {J} _ {i} \mathrm{d} \boldsymbol {i} \tag {1.8}
$$

with the rst term is caused by the mechanical movement of the rotor and the second term is due to the variation of the current. 

# 1.1.2. The relationship between the coupling electrical energy variation, the mechanical energy variation and the magnetic energy variation

For the mechanical energy variation, there is: 

$$
\mathrm{d} E _ {\Omega} = \boldsymbol {T} _ {q} ^ {T} \mathrm{d} \boldsymbol {\Omega} \tag {1.9}
$$

with $\textstyle \mathbf { \mathcal { T } } _ { q }$ the mechanical torque acting on the particular shaft with movement of Ω. 

For the magnetic energy variation, there is unfortunately no easy equation available. Nevertheless, by considering the magnetic energy as a state function, the following formulation can be used: 

$$
\mathrm{d} E _ {m} = E _ {m} (\boldsymbol {i} + \mathrm{d} \boldsymbol {i}, \boldsymbol {\Omega} + \mathrm{d} \boldsymbol {\Omega}) - E _ {m} (\boldsymbol {i}, \boldsymbol {\Omega}) \tag {1.10}
$$

with $E _ { m }$ is a state function of the state variables i, Ω. (1) 

By considering the magnetic energy as function of the state variables i, Ω, a formulation of the total dierential d $E _ { m }$ equation 1.10 as sum of partial dierentials can be obtained: 

$$
\mathrm{d} E _ {m} = \left(\boldsymbol {J} _ {\Omega}\right) ^ {\mathrm{T}} \mathrm{d} \boldsymbol {\Omega} + \left(\boldsymbol {J} _ {i}\right) ^ {\mathrm{T}} \mathrm{d} \boldsymbol {i} \tag {1.11}
$$

with the element of the Jacobian vector: 

$$
J _ {\Omega , n} = \frac {\partial E _ {m}}{\partial \Omega_ {n}} \tag {1.12}
$$

$$
J _ {i, n} = \frac {\partial E _ {m}}{\partial i _ {n}}
$$

According to the energy conservative laws (Equation 1.1) and by considering the particular energy variation (Equation 1.8, 1.9 and 1.11), for the electrical state variables, there is: 

$$
\boldsymbol {i} ^ {\mathrm{T}} \mathbf {J} _ {i} \mathrm{d} \boldsymbol {i} = (\boldsymbol {J} _ {i}) ^ {\mathrm{T}} \mathrm{d} \boldsymbol {i} \tag {1.13}
$$

and for the mechanical state variables, there is: 

$$
\boldsymbol {i} ^ {\mathrm{T}} \mathbf {J} _ {\Omega} \mathrm{d} \boldsymbol {\Omega} = \boldsymbol {T} _ {q} ^ {\mathrm{T}} \mathrm{d} \boldsymbol {\Omega} + (\boldsymbol {J} _ {\Omega}) ^ {\mathrm{T}} \mathrm{d} \boldsymbol {\Omega} \tag {1.14}
$$

# 1.1.3. The relationship between the coupling electrical energy variation, the mechanical energy variation and the magnetic co-energy variation

By using the equations above, there is a more complicate relationship for the mechanical state variables, which is however more important for the electromechanical conversion process. This can be easily solved, if a new state quantity named magnetic co-energy is introduced, which is: 

$$
E _ {m} ^ {\prime} = \int \boldsymbol {\psi} ^ {\mathrm{T}} \mathrm{d} \boldsymbol {i} = \boldsymbol {i} ^ {\mathrm{T}} \boldsymbol {\psi} - E _ {m} \tag {1.15}
$$

With this new state quantity, the total dierential of the magnetic energy can be formulated as: so that: 

$$
\begin{array}{l} \mathrm{d} E _ {m} = \boldsymbol {\psi} ^ {\mathrm{T}} \mathrm{d} \boldsymbol {i} + \boldsymbol {i} ^ {\mathrm{T}} \mathrm{d} \boldsymbol {\psi} - \mathrm{d} E _ {m} ^ {\prime} \\ = \boldsymbol {\psi} ^ {\mathrm{T}} \mathrm{d} \boldsymbol {i} + \boldsymbol {i} ^ {\mathrm{T}} \mathbf {J} _ {\Omega} \mathrm{d} \boldsymbol {\Omega} + \boldsymbol {i} ^ {\mathrm{T}} \mathbf {J} ^ {i} \mathrm{d} \boldsymbol {i} - (\mathbf {J} _ {\Omega} ^ {\prime}) ^ {\mathrm{T}} \mathrm{d} \boldsymbol {\Omega} - (\mathbf {J} _ {i} ^ {\prime}) ^ {\mathrm{T}} \mathrm{d} \boldsymbol {i} \tag {1.16} \\ = \left(\boldsymbol {\psi} ^ {\mathrm{T}} + \boldsymbol {i} ^ {\mathrm{T}} \mathbf {J} ^ {i} - \left(\boldsymbol {J} _ {i} ^ {\prime}\right) ^ {\mathrm{T}}\right) \mathrm{d} \boldsymbol {i} + \left(\boldsymbol {i} ^ {\mathrm{T}} \mathbf {J} _ {\Omega} - \left(\boldsymbol {J} _ {\Omega} ^ {\prime}\right) ^ {\mathrm{T}}\right) \mathrm{d} \boldsymbol {\Omega} \\ \end{array}
$$

with the new Jacobian vector: 

$$
J _ {\Omega , n} ^ {\prime} = \frac {\partial E _ {m} ^ {\prime}}{\partial \Omega_ {n}} \tag {1.17}
$$

$$
J _ {i, n} ^ {\prime} = \frac {\partial E _ {m} ^ {\prime}}{\partial i _ {n}}
$$

Equation 1.14 is then simplied to: 

$$
\left(\boldsymbol {J} _ {\Omega} ^ {\prime}\right) ^ {\mathrm{T}} \mathrm{d} \boldsymbol {\Omega} = \boldsymbol {T} _ {q} ^ {\mathrm{T}} \mathrm{d} \boldsymbol {\Omega} \tag {1.18}
$$

while a simple form of Equation 1.13 is still got: 

$$
\boldsymbol {\psi} ^ {\mathrm{T}} \mathrm{d} \boldsymbol {i} = \left(\boldsymbol {J} _ {i} ^ {\prime}\right) ^ {\mathrm{T}} \mathrm{d} \boldsymbol {i} \tag {1.19}
$$

# 1.2. The eld quantity approach

For the eld quantity approach, the current density within the whole machine is chosen as the electrical state variables, which is considered as a physical vector $\vec { J } ( x , y , z , t )$ . 

To formulate the electromechanical energy conversion process can be formulated using the eld quantities, the Poynting theorem is used, which supposes the electrical power being calculated as: 

$$
\frac {\mathrm{d} E _ {e}}{\mathrm{d} t} = - \int \operatorname{div} (\vec {\boldsymbol {E}} \times \vec {\boldsymbol {H}}) \mathrm{d} V \tag {1.20}
$$

By considering the vector calculus: 

$$
\operatorname{div} (\vec {\boldsymbol {E}} \times \vec {\boldsymbol {H}}) = \vec {\boldsymbol {H}} \cdot \operatorname{rot} \vec {\boldsymbol {E}} - \vec {\boldsymbol {E}} \cdot \operatorname{rot} \vec {\boldsymbol {H}} \tag {1.21}
$$

together with the maxwell equations (2) 

$$
\operatorname{rot} \vec {\boldsymbol {E}} = - \frac {\mathrm{d} \vec {\boldsymbol {B}}}{\mathrm{d} t} \tag {1.22}
$$

$$
\mathrm{rot} \vec {H} = \vec {J}
$$

and the material equation: 

$$
\vec {\boldsymbol {E}} = \rho \vec {\boldsymbol {J}} \tag {1.23}
$$

Equation 1.20 changes to: 

$$
\mathrm{d} E _ {e} = \int \rho | \vec {\boldsymbol {J}} | ^ {2} \mathrm{d} V \mathrm{d} t + \int \vec {\boldsymbol {H}} \mathrm{d} \vec {\boldsymbol {B}} \mathrm{d} V = \mathrm{d} E _ {e, d} + \mathrm{d} E _ {e, c} \tag {1.24}
$$

with the rst term the dissipative electrical energy d $E _ { e , d }$ and the second term the coupling electrical energy d $E _ { e , c }$ . 

To get a better understanding of the relationship between the lumped quantities and the eld quantities, it is reasonable to introduce the magnetic vector potential, which is dened as: 

$$
\vec {B} = \nabla \times \vec {A} \tag {1.25}
$$

By consideration of the vector calculus: 

$$
\vec {\boldsymbol {a}} \cdot (\nabla \times \vec {\boldsymbol {b}}) = \vec {\boldsymbol {b}} \cdot (\nabla \times \vec {\boldsymbol {a}}) - \nabla \cdot (\vec {\boldsymbol {a}} \times \vec {\boldsymbol {b}}) \tag {1.26}
$$

the second term of Equation 1.24 changes to: 

$$
\int \vec {H} \mathrm{d} \vec {B} \mathrm{d} V = \int \vec {J} \mathrm{d} \vec {A} \mathrm{d} V - \int \nabla \cdot (\vec {H} \times \vec {A}) \mathrm{d} V \tag {1.27}
$$

which is reduced to: 

$$
\int \vec {H} \mathrm{d} \vec {B} \mathrm{d} V = \int \vec {J} \mathrm{d} \vec {A} \mathrm{d} V \tag {1.28}
$$

since: 

$$
\int \nabla \cdot (\vec {H} \times \vec {A}) \mathrm{d} V = \int \vec {H} \times \vec {A} \mathrm{d} \vec {S} = 0 \tag {1.29}
$$

if the integration surface is chosen at the innite far place [71]. 

Equation 1.24 is then: 

$$
\mathrm{d} E _ {e} = \int \rho | \vec {\boldsymbol {J}} | ^ {2} \mathrm{d} V + \int \vec {\boldsymbol {J}} \mathrm{d} \vec {\boldsymbol {A}} \mathrm{d} V = \mathrm{d} E _ {e, d} + \mathrm{d} E _ {e, c} \tag {1.30}
$$

with the rst term the dissipative electrical energy and the second term the coupling electrical energy. (3) 

# 1.3. Winding: a double-way bridge

Comparing Equations 1.5 and 1.30 for the formulation of the coupling electrical energy d $E _ { e , c }$ : 

$$
\mathrm{d} E _ {e, c} = \boldsymbol {i} ^ {\mathrm{T}} \mathrm{d} \boldsymbol {\psi} = \int \vec {\boldsymbol {J}} \mathrm{d} \vec {\boldsymbol {A}} \mathrm{d} V \tag {1.31}
$$

It is clear that the lumped quantity i is corresponding with the eld quantity $\vec { J }$ and the lumped quantity ψ is corresponding with the eld quantity A~. ${ \vec { A } } .$ 

Actually, in case of 2D, there are following simple relationship between these quantities: 

$$
i _ {k} = \int_ {\text {w,   l,   f}} J _ {z} \mathrm{d} s _ {n} \tag {1.32}
$$

$$
\psi_ {n} = \frac {w _ {k} l _ {z}}{S _ {n}} \int A _ {z} \mathrm{d} s _ {n}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a532c9d3b13d61733c059c597139bd6d5d2b4bf07e585b714107563e3c133b6c.jpg)



(a) Coupling energy using $B _ { x }$ and $H _ { x }$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/00dc08f82b6f6befd3e41a9a6836f4ac0795d135f0438ccd6caf52ef778a29da.jpg)



by (b) Coupling energy calculated by using $A _ { x }$ and $J _ { x }$



Figure 1.2.: Dierent methods for the calculation of the electrical coupling energy by xed rotor position (for the illustration only one component of the eld quantities is used)


where $w _ { k }$ and $S _ { n }$ are the total number of turns and cross-sectional area of winding k respective. The formulation for the phase ux linkage is widely used in 2D nite element software [85]. 

Obviously, there should be one component within the electrical machine, which plays the role of a bridge linking the lumped and eld quantities. Since there are two electrical lumped quantities $( \psi$ and i) and two magnetic eld quantities $( \vec { A }$ and $\vec { J } )$ , it should be two bridges, linking the quantities completely. 

Fortunately, these two functionalities, namely: 

 changing the phase current i into spatial distributed current density ${ \vec { J } } ,$ 

 and changing the spatial distributed magnetic vector potential $\vec { A }$ into phase ux linkage $\psi$ , 

are realized by the same component: the multi-phase symmetrical winding. Therefore, the multi-phase symmetrical winding can be seen as the key component of the electrical machine during the electromechanical energy conversion process. 

This fact can be clearly illustrated in gure 1.3, where a detailed discussion and mathematical modeling of the block Symmetrical multi-phase Winding is occurred in chapter 5. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/4883599dab3659cfe5cbcc1cfc1764e54b44df92e25f31c3f75dfd4bb410f116.jpg)



Figure 1.3.: The double roles of the multi-phase symmetrical winding


# 2. The impacts of the winding on the machine performance

As discussed in the previous chapter, the multi-phase symmetrical winding is the key component during the electromechanical energy conversion process. It impacts the machine performance through the following ways. 

# 2.1. The winding insulation

The insulation of the winding species the operation voltage and temperature level of the winding. For the permanent magnet synchronous machine where the air-gap ux density is constant, the induced winding voltage is linearly related to the rotor speed $( \vec { E } _ { v } = \vec { v } \times \vec { B } )$ . and the current is directly proportional to the electromagnetic force $( \vec { F } = i \vec { l } \times \vec { B } )$ . Because the winding temperature is linearly related to the winding current losses $( \Delta T _ { w } = R _ { w , t h } P _ { w , l o s s } )$ where the winding current losses is direct proportional to the square of the current $( P _ { w , l o s s } = R _ { w , e l } i ^ { 2 } )$ . The insulation of the winding denes the max. speed as well as the max. torque of the electrical machine and thus the max. power density. This can be seen from gure 2.1 which shows the impacts of the winding insulation on the power density and eciency of the machine. 

# 2.2. The number of turns

In general, a winding is a serial and/or parallel connection of coils with the same number of turns. For a given winding topology, the number of turns of the winding is linearly related to the number of turns of the coils. Unlike the winding insulation, changing the number of turns does not aect the max. power density of the machine. However, it has a signicant impact on the shape of the speed-torque operation map. For a given max. phase current and voltage, an increasing of the number of turns increases the max. electromagnetic force linearly $( \vec { F } = w _ { k } i \vec { l } \times$ $\vec { B } )$ . However, the max. rotor speed is decreased hyperbolically $( u =$ $w _ { k } l \vec { v } \times \vec { B } )$ . This can be seen from gure 2.2 which shows the impacts of the number of turns on the max. speed-torque operation curve of the machine. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/7189f7844831dcf6f9cfa34d32bbe62b6bccf839778507108355df33bf0732a3.jpg)



Figure 2.1.: impacts of the winding insulation on the power density and eciency of the machine [32]


# 2.3. The winding production method

Two winding properties depend strongly on the winding production method: the slot lling factor (gure 2.3) and the end-winding (gure 2.4). All this has direct impacts on the machine performance. 

Winding of high slot lling factor means larger copper cross section and therefore smaller electrical and thermal resistance. This results in a better eciency and power density. The electrical resistance and the thermal conductivity (according to [64]) are given: 

$$
R _ {c, e l} = \rho \frac {l}{A}, \quad \kappa_ {w, t h} = \kappa_ {p} \frac {(1 + f _ {c}) \kappa_ {c} + (1 - f _ {p}) \kappa_ {p}}{(1 - f _ {c}) \kappa_ {c} + (1 + f _ {p}) \kappa_ {p}}
$$

where A is the copper cross section, $\kappa _ { c }$ and $f _ { c }$ are thermal conductivity and lling factor of copper, $\kappa _ { p }$ and $f _ { p }$ are thermal conductivity and lling factor of the insulation material. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/b9597d30fcef8f70f3a02a30c10a556948d544655a99fbdb6400aea88720a72c.jpg)



(a) Winding with large number of turns


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/579aebb222893f0dfd808f0146229056b103d757615eb6e8344ead4c40f5ba9c.jpg)



(b) Winding with small number of turns



Figure 2.2.: impacts of the number of turns on the max. speed-torque operation curve [70]


For the same designed space, winding of short end-winding means more space of iron stack and therefore more area for the torque generation. This is because the electromechanical energy conversion occurs not in the air-gap area of the iron stack. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/15124b669a7155c84865e4ae188d6da9ca05ca4ca852f0eaedff9b301856c437.jpg)



Winding nozzle



(a) conventional needle-winding method


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/fdd2226da98498a3533142f02afd9b63479e21040f51a5f00c32ca97d27a7d9d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/fdfc970f703345c3e4e5244664a8a62e6597a716baacf3d4b20cfe92d4510c36.jpg)



(b) Separated core with needle-winding method


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e64410fadd3f0543c0c53971f8585af83cf3e50562623510ffb04c19582db721.jpg)



(c) Connected core with needle-winding method



Figure 2.3.: Impacts of the winding production method on slot lling factor [1]


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e2925dc3793b02665b3df3de7668266be48328187792d9a12beae28d53ec1876.jpg)



(a) Winding with conventional coils of round wire


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/5b9eb0bf967704e1d56578048d32451c5ee2dc73536817b95512fa2fb3e0504b.jpg)



(b) Winding with Hiarpin-Coil of rectangular wire



Figure 2.4.: Impacts of the winding production method on the endwinding [38]


# 2.4. The winding topology

The winding topology describes how the winding is distributed among the stator circumference. A well-designed winding topology can convert a sinusoidally varied current system $\underline { { i } } \mathrm { e } ^ { j \omega t }$ into a sinusoidal MMF space harmonic $\Theta _ { k } \mathrm { e } ^ { j ( k x + \omega t ) }$ with a possible large amplitude of the working harmonic and possible small amplitude of sub- and over-harmonics. This is the precondition that the electrical machine supplies constant power (electrical and mechanical) with high eciency. Thus the winding topology impacts the machine performance in various ways which is discussed in the next sections in detail. 

# 2.4.1. Torque quality

The Impacts of the tooth coil winding of dierent layer (1-, 2- and 4- layer) on torque quality of a 12 slots/10 Poles interior PM machine is discussed by various authors [81, 55]. 

Wang et al. [81] show that for high current excitation, the machine with 4-layer winding performs the highest torque although the winding factor of the working harmonic of this winding topology is the lowest. This is contrary to the classical theory because it is claimed that higher winding factor of the working harmonic results in higher torque. It is to mention that the classical theory is valid for the fundamental harmonic winding topology (fundamental harmonic as working harmonic) without considering the saturation of the iron parts. Both of these assumptions are not met by the investigated winding since the working harmonic of the winding is the 5-harmonic and the existence of the sub-harmonic causes the saturation of iron part. As the 4-layer winding has the smallest subharmonics contents, its iron part is less saturated. The same Eect has been reported by Reddy et al. [55] which shows a 5.2% improvement of the torque density from a 2-layer winding to a 4-layer winding for the same peak current excitation. 

Wang et al. [81] also show that for the peak current excitation, the torque ripple of the investigated 12 slots/10 poles interior machine can be reduced under 2% by using the 4-layer winding. For the single- and double-layer winding, this value is 3.9% and 5.0% respectively. The same eect is observed by Reddy et al. [55] who claim that the torque ripple of the investigated 12 slots/10 poles interior machine can be reduced from 18.5% (1-layer winding) to 5.0% (2-layer winding) towards 3.5% (4- layer) at base speed operation range and from 51.2% (1-layer winding ) to 20.6% (2-layer winding) towards 8.9% (4-layer winding) at ux-weakening operation range. 

# 2.4.2. Torque-speed operation range

The impacts of the winding topology on the torque-speed operation range is discussed by various authors [22, 70]. 

For the same rated load current and voltage conditions, Dajaku et al. [22] investigate the impacts of two dierent winding topologies on the torque-speed range of an interior PM machine with 10 poles. The rst winding is a conventional 12 slots double-layer winding with coils of the same number of turns and the second winding is a novel 18 slots doublelayer winding with coils of a dierent number of turns. The results show that even the new winding topology is with a lower winding factor of the working harmonic (0.760 vs. 0.933), with a well-chosen number of turns per phase (19/14 instead of 30), the new machine is with a wider torque-speed operation range. In the eld weakening operation range, an increasing of the output power for about more than 20% can be achieved (gure 2.5). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/361424b93bb71defb622035c6eb1d75178a956ad53a88a6f1414be96a03a24a7.jpg)



(a) Torque-speed curve


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/f7709881f03545d56124cfecc3b0ea2e0737cd96f269cf6f089bf2c7c8adf375.jpg)



(b) Power-speed curve



Figure 2.5.: Impacts of the winding topology on the torque-speed operation range [22]


# 2.4.3. Inductance

The impacts of the winding topology on machine inductance are discussed by various authors [27, 22]. 

The investigation by El-Refaie et al. [27] shows that for the investigated surface permanent magnet synchronous machine, single-layer tooth coil winding generally performs much higher self-inductance (up to 59% when compared with its double-layer counterpart) but negligible small mutual inductance between the phase. 

For the case of interior PM synchronous machine, Dajaku et al. [22] investigate the impacts of the winding topology on the d/q-inductances, which are characteristic quantities for the reluctance torque generation. The investigation shows that winding with small sub-harmonic contents shows larger $\mathrm { d } / \mathrm { q }$ inductance dierence, even the winding factor of the working harmonic is smaller (gure 2.6). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/0842f91e624c57ece7e57f3acc311897e96c54e375a895140bf8e53e6d5da043.jpg)



(a) Value of $\mathrm { d } / \mathrm { q }$ inductance of dierent winding topology


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/b823d01fe9e5aa8c75aa0c420c21af66d97d0be656889e929e26547403c87d48.jpg)



(b) Ratio of $\mathrm { d } / \mathrm { q }$ inductance of dierent winding topology



Figure 2.6.: Impacts of the winding topology on the d/q-inductances [22]


# 2.4.4. Electromagnetic losses

# 2.4.4.1. Winding copper losses

If the eddy current eects within the winding conductor as well as the saturation of the iron part are neglected, by producing the same torque, for the case of a permanent magnet synchronous machine, the copper losses of the stator winding are inversely proportional to the winding factor squared [46]. For the case of an induction motor, this is inversely proportional to the winding factor cubed. This can be simply explained as follows: 

The current sheet amplitude of the working harmonic is proportional to the winding factor $\hat { K } _ { s , \nu } \sim \xi _ { \nu }$ and the surface force density is proportional to the stator current sheet and rotor ux density $\overline { { f } } \sim \hat { K } _ { s , \nu } \cdot \hat { B } _ { r , \nu }$ . For the case of a permanent magnet synchronous machine, the rotor ux density $\hat { B } _ { r , \nu }$ is independent on the stator current sheet and for the case of an induction motor, the rotor ux density linearly depends on the stator current sheet $\hat { B } _ { r , \nu } \sim \hat { K } _ { s , \nu }$ . 

# 2.4.4.2. Iron losses

The impacts of winding topology on the iron losses are discussed by various authors [28, 79, 22]. 

For the case of surface permanent magnet machine, Fornasiero et al. [28] investigate the impacts of dierent winding topology (dierent number of slots, dierent number of phases and dierent working harmonic order) on the rotor iron losses. The results (gure 2.7) show that the number of slots, as well as the working harmonic order, were found to have strong impacts on the rotor iron losses: for the same working harmonic order, the larger the stator number of slots, the lower the rotor iron losses; for the same number of stator number of slots, the larger the working harmonic order, the larger the rotor iron losses. Furthermore, it is claimed that the number of phases has only a minor eect on the rotor iron losses. 

Von Pngsten et al. discussed in [79] the impacts of dierent winding topology (the same working harmonic but dierent number of slots and dierent coil pitch) on the iron loss of an interior PM machine of 6 poles. The investigation shows that (gure 2.9), the number of stator slots has the signicant impact on the stator and rotor iron losses, both in the absolute value of the losses and the loss distribution, especially in the ux-weakening operation range. A larger number of stator slots leads to larger total iron losses and lower rotor iron losses. The coil pitch is found to have only a minor eect on the iron losses. 

For winding working working with over-harmonic MMF, the investigation of Dajaku et al. [22] shows that (gure 2.8), the smaller the MMF sub-harmonic contents, the lower the stator and rotor iron losses. 

<table><tr><td>Configuration</td><td>3-phase winding rotor losses (W)</td><td>5-phase winding rotor losses (W)</td></tr><tr><td>30/4</td><td>60.9</td><td>52</td></tr><tr><td>30/16</td><td>107.8</td><td>88.4</td></tr><tr><td>30/32</td><td>305.8</td><td>294.1</td></tr></table>


(a) Stators of 30 slots


<table><tr><td>Configuration</td><td>3-phase winding rotor losses (W)</td><td>7-phase winding rotor losses (W)</td></tr><tr><td>42/4</td><td>32.1</td><td>22.9</td></tr><tr><td>42/20</td><td>62.6</td><td>41.6</td></tr><tr><td>42/44</td><td>182.5</td><td>171.8</td></tr></table>


(b) Stator of 42 slots



Figure 2.7.: Impacts of the winding topology on the iron loss of surface PM machine [28]


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/39d7b055a28552cd54099995a1364170c72f4d2ea608afe6132090e9f22f1086.jpg)



(a) Stator iron loss


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/14fa092a5f20130d64f66cfb627d9acad71ae84377f26eafbb56f348216409c4.jpg)



(b) Rotor iron loss



Figure 2.8.: Impacts of the over-harmonic winding topology on the iron loss of interior PM machine [22]


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/90c1bc61e042b0380e433d377c29f4fda07cc5538b98332c991584c933e74133.jpg)



(a) Stators under investigation


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/3eb08cff1d1d25c89736586188dfcf31e35f4aab6ff5c7b7014d650f6519255a.jpg)



(b) Iron losses



Figure 2.9.: Impacts of the fundamental harmonic winding topology on the iron loss of interior PM machine [79]


# 2.4.4.3. Permanent magnet eddy current losses

Surface permanent magnet machine The impacts of winding topology on the surface PM eddy current losses were discussed by various authors [20, 42]. 

Dajaku et al. [20] show that a reduction of the total PM eddy current losses of a 12 slots/10 poles surface permanent magnet synchronous machine up to 67% can be achieved by using the novel winding topology with coils of a dierent number of conductor per coil side. Such winding topology reduces the sub-harmonic contents signicantly (gure 2.10). 

The same eect has been reported by Kim et al. [42], who investigate two surface PM machines of 12 slots/10 poles and 18 slots/16 poles with dierent winding topology (classical double-layer winding with coils of the same number of turns and 4-layer winding with coils of a dierent number of turns). The investigation shows that, for the 12 slots/10 poles machine, a 45% improvement of the permanent magnet eddy current losses can be achieved and for the 18 slots/16 poles, a 16% improvement of the permanent magnet eddy current losses can be achieved. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/4adfdfc27ecd8e6575650ff4289d7eeb0e8b35d5458c13cb880cb007d9f95ef4.jpg)



(a) Winding spectrum


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/eb86a757188264e87a4c86d5b88117c0d8ffc518e773a88ef9c196dd2998a845.jpg)



(b) Eddy current losses



Figure 2.10.: Impacts of the winding topology on the surface permanent magnet eddy current losses [20]


Interior permanent magnet machine The impacts of winding topology on the interior PM eddy current losses were discussed various authors [67, 22]. 

The same two windings as given in [42] were investigated by Sun et al. [67] for an interior PM machine, and the results also show a signicant reduction of the permanent magnet eddy current, up to 48% improvement is mentioned by using the 4-layer winding with coils of a dierent number of turns. The same technique was applied by Dajaku et al. [22] for a 18 slots/10 poles interior PM machine, which is compared with its 12 slots/10 poles counterpart (gure 2.11). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/b8f817a049bbf4fcf992ece8fb730739989f0f578e42fabe265f7829e0d33a94.jpg)



(a) Eddy current vs rotor speed


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/5d13993b87fc2ce43274f3fb99546fdd63ffca7296d586b4f28d85a0380c2ab6.jpg)



(b) Eddy current distribution



Figure 2.11.: Impacts of the winding topology on the interior permanent magnet eddy current losses [22]


# 3. An introduction to the winding topology

# 3.1. The understanding of the winding topology

In this thesis, the term winding topology is used to completely describe the properties of the winding, which can be understood from the geometrical as well as the electromagnetic aspect. 

# 3.1.1. The geometrical point of view

From the geometrical point of view, a multi-phase winding is nothing but a set of spatially distributed coils where each coil is with a particular number of turns, coil pitch, and winding direction. Coils of the same winding direction are connected to each other to form the so-called coil group and coil groups of dierent winding directions are connected to each other to form a single-phase winding. In general, multiple singlephase windings are connected to each other, resulting in a multi-phase winding. 

From this point of view, to completely describe the geometrical properties of the winding topology, the following information should be known: 

 the position of each coil, 

 the coil pitch of each coil, 

 the number of turns of each coil, 

 the connection of the coils of the same phase, 

 and the connection of the single-phase windings of the multi-phase winding. 

# 3.1.2. The electromagnetic point of view

From the electromagnetic point of view, a multi-phase winding is a set of spatially distributed conductors, which are fed by currents of dierent phases. This results in a one-dimensional spatially distributed and time-varying MMF. By using the Fourier analysis, the space and time dependent MMF distribution can be formulated as a superposition of space harmonics of dierent amplitudes and orders. 

From this point of view, to completely describe the electromagnetic properties of the winding topology, the following information should be known: 

 the number of conductors within each slot, 

 the phase aliation of each conductor, 

 and the winding direction of each conductor. 

# 3.2. A short introduction to the terminology

In the eld of winding topology, a great number of terminology can be found in the literatures(1), which describe the winding topology from dierent aspects. The main purpose of this section is: 

 to give a short overview of the existing terminology, 

 and to introduce some new terminology, which is beyond the classical terminology and will be used for the novel winding topology proposed in this thesis. 

# 3.2.1. The existing terminology for the description of winding topology

Distributed & tooth coil winding, overlapping & non-overlapping winding Such Terminology describes the winding topology according to whether the coil pitch is equal to one slot pitch. The rst terminology describes this property explicitly, while the second terminology describes this property implicitly. It is to notice that the end-winding of the tooth coil winding is non-overlapping, while the end-winding of the distributed winding overlaps. Nevertheless, such implicit terminology is not suitable for winding topology treatment method since the end-winding is not considered. 

Single- & double-layer winding, all teeth & alternate teeth wound winding Such Terminology describes the winding topology according to the number of coil sides within one slot. The terminology single-& double-layer winding is conventionally used for distributed winding, while the terminology all teeth & alternate teeth wound winding is used for tooth coil winding. 

Integer & fractional slot winding Such Terminology describes the winding topology according to whether the so-call number of slot per pole and phase q is an integer number: 

$$
q = \frac {N _ {s}}{p m}
$$

This is a quite popular terminology used in the eld of the winding topology design method. For some winding topology design methods, such number plays a central role. However, it will be shown in the next chapter that winding topology design methods relying on such number have a lack of fundamental theoretical basis and can be replaced by more elegant methods. Moreover, such number gives no information about the geometric and electromagnetic properties of the winding. It is to mention that, the two main types of classical winding topology treatment method: the star of slots method and the Kauders' systematics are not based on such number. 

Full & fractional pitch winding Such Terminology describes the winding topology according to whether the coil pitch is equal to the pole pitch. It is to notice that, for the case of tooth coil winding where the coil pitch is equal to the slot pitch, such winding can not be a full pitch winding. 

$\mathbf { a / b } , \mathbf { \beta < a - b - c - d > _ { k } }$ Such Terminology tries to describe the winding topology by a set of numbers, which is specic for the tooth coil winding of permanent magnet machine. For the rst terminology, a is the number of stator slots, and b is the number of rotor permanent magnets. The second terminology is rstly introduced by H. Mosebach [50] and further improved by W.-R. Canders et al. [12]. Five numbers are used to fully describe the winding topology, where a is the number of coils, b is the number of coils per winding zone, c is the number of coil groups, d is the number of permanent magnets, and k is the number of coil sides per slot. 

# 3.2.2. Terminology used in this thesis for the description of winding topology

Fundamental & over-Harmonic Winding Such terminology gives the information about the working harmonic of the winding. For the fundamental harmonic winding, the fundamental MMF harmonic of the winding is used for torque production (2), while for over-harmonic winding, one of the MMF over-harmonics is used for torque production. It is to notice that, the fundamental or over-harmonic winding can be distributed or tooth coil winding, integral or fractional slot winding and single or double-layer winding. 

Classical winding topology The term classical winding topology is understood as winding with coils of the same number of turns and coil pitch. Furthermore, for each coil, the number of conductors of both coil sides is the same. Such winding can be single or double-layer winding, distributed or tooth coil winding. 

Single- & multi-tooth coil winding The single-tooth coil winding is understood as winding with coils of coil pitch equal to single tooth pitch (The tooth pitch is equal to slot pitch.). For the case of multi-tooth coil winding, the coil pitch is equal to multiple tooth pitch. 

Multi-layer winding topology The term multi-layer winding topology is understood as winding where there are more than two coil sides per slot. 

Multi-coil winding topology The term multi-coil winding topology is understood as double-layer winding where the coils are with dierent coil pitch and number of turns. 

Multi-conductor winding topology The term multi-conductor winding topology is understood as double-layer winding where coils are with a dierent number of conductors per coil side. 

# 3.3. The two main problems for winding topology treatment

In the eld of winding topology treatment, there are two main types of problem: the winding topology analysis problem and the winding topology design problem, which can be seen as to solve a direct and an inverse problem. 

# 3.3.1. Winding topology analysis

The Winding topology analysis begins with a given winding topology (in the form of a winding scheme) and is with the objective to investigate the quality of the winding topology. The winding factor harmonic spectrum is used to characterize the quality of the winding topology. This problem is considered as solved if the winding factor harmonic spectrum is obtained. 

# 3.3.2. Winding topology design

The Winding design begins with the desired pole pairs $p ,$ the available number of current phases m and an assumed number of slots $N _ { s }$ and is with the objective to nd out the optimal winding topology under dierent constraints. The optimal winding topology depends on the chosen criteria, which can be the max. possible winding factor of the working harmonic, the best possible winding factor harmonic spectrum or the simplest structure of the winding topology and so on. 

The winding topology design problem as solving an inverse problem is more dicult as its counterpart. A simple example is given as follows, which show that even for a problem with strong constraints, an ecient algorithm is needed to nd out a good result.s 

Suppose that a 3-phase single-layer winding with 12 slots is asked, which should work with a 10 poles permanent magnet rotor. For the simplest case that the number of conductors per slot is the same, the entire possible winding topology is given as: 

$$
N _ {w} = (2 m) ^ {N _ {s}} = 6 ^ {1 2} = 2, 1 7 6, 7 8 2, 3 3 6 \tag {3.1}
$$

As for each slot, the phase aliation of the conductor can be freely chosen from the following 6 possibilities: 

$$
\phi_ {k} \in \{A, \overline {{A}}, B, \overline {{B}}, C, \overline {{C}} \} \tag {3.2}
$$

By further constraining the problem that the phase aliation should be evenly used (This can be interpreted as a symmetrical condition.), the total number of possibility reduces to: 

$$
N _ {w} = N _ {s}! = 1 2! = 4 7 9, 0 0 1, 6 0 0 \tag {3.3}
$$

which is still an enormous number. 

It is to underline that, the number of conductors within each slot is without of consideration by the discussion above. It is reasonable to image that, if this additional design parameter is considered, the number of possibilities explodes. For this reason, this design is always outside consideration by the classical design methods from the beginning, making the problem treatable. However, it will be shown later that The method introduced in this thesis considers this design parameter naturally and the optimal number of turns of each coil can be calculated by solving a system of linear equations. 

# 3.4. A historical review of the research activities

Since the invention of the multi-phase rotating eld machine, it is recognized that the impacts of the winding topology on the machine performance are very strong and the problem of winding topology design is dicult to solve. Thus eorts are continually made in the eld of winding topology design. Either from the time aspect or the research topic aspect, such methods can be naturally separated into two parts. 

# 3.4.1. Treatment of fundamental harmonic winding topology till the 1950s

From the historical point of view, the rst research activities begin with the invention of the rotating eld machine by N. Tesla [72] in the year 1888 (3) and end with the publication of H. Sequenz's book about armature winding of multi-phase machines [63] in year 1950s (4). 

During this period, fundamental harmonic winding with distributed coils is mainly considered. The primary design objective is to maximize the winding factor of the fundamental harmonic. The winding factors of the over-harmonics are almost out of consideration since the impacts of the over-harmonics on the machine performance is very small. This can be explained quite simple as follows: 

There is a proportional factor of $\textstyle { \frac { 1 } { \nu } }$ between the winding factor and the MMF, where ν is the harmonic order. Furthermore, between the MMF and the B~ -eld in the air-gap, there is another proportional factor of $\frac { 1 } { \delta }$ where δ is the magnetic eective air-gap. Therefore, a proportional factor of $\textstyle { \frac { 1 } { \nu } }$ links the winding factor to the ${ \vec { B } } .$ -eld in air-gap. This means that the higher the harmonic order, the smaller the magnetic energy of the harmonic. An electrical Machine with such winding is named as a fundamental harmonic machine in the literature, which can be accurately described by the fundamental harmonic theory. 

It is also interesting to notice that, during this period, graphical design methods or design methods with simple numerical calculation are preferred due to the lack of computing power. 

# 3.4.1.1. The great success in the achievement of winding topology treatment methods

During this period, a great success in the achievement of winding topology treatment methods is obtained, which can be summarized as follows: 

 A central research topic is to nd a unied method for the treatment of the winding topology, which is almost done by the method introduced by R. Richter [59, 58]. He is considered as the rst one who does the research in this eld systematically with theoretical consideration. The methods introduced by him is named as the star of slots method nowadays in the literature, which can be found in almost every textbook about design of electrical machines. The star of slots method can handle the two problems of winding topology treatment at the same time, and most of the problems can be suciently solved. Furthermore, it is very suitable to be used as a graphical design tool by introducing the complex phasor notation for the induced EMF. Due to these facts, this method is widely spread leading to some deduced forms published [73, 6, 63]. 

 For the special case of double-layer fractional slot winding, which the star of slots method cannot completely solve, many research investigations were done from 1931 till 1947. Dierent design methods introduced by various authors can be found in [10, 83, 77, 54, 62]. All these methods have two common points: the number of slot per pole per phase q plays a central role in the design process, and they are based on the geometrical consideration of the winding topology (In contrast, the star of slots method is primarily based on electromagnetic consideration.). The target of such methods is to place the coils among the stator circumference as symmetrical as possible. However, a precise denition of the symmetry is never given. Due to these drawbacks, such methods never attract great attentions within the research group. Nowadays, it is hard to nd such methods in newly published textbooks. 

 An another signicant achievement during this research period is the introduction of the systematic of the 3-phase winding by W. Kauders [40, 41]. As a winding topology analysis method, this method decomposes the total winding factor into a multiplication of several partial winding factors. Each partial winding factor describes a particular geometrical aspect of the winding topology. More information about the impacts of each winding structure on its electromagnetic property can be obtained. 

With this systematic, the special case of double-layer fractional slot winding can be suciently solved. However, this method is almost neglected since its rst publication (5). This is because the method introduced by W. Kauders is a systematically organized enumeration method. The major drawback of an enumeration method is that a great number of cases may take place, where each of them needs to be analyzed in the same way. This property makes an enumeration method applicable only when sucient computing power is available. 

In general, a great success in respect of the theory and methodology of winding topology is achieved. Two dierent types of method are introduced by R. Richter and W. Kauders, which consider the winding topology from electromagnetic and geometrical aspect respectively. Since then, No more fundamental idea in this eld is reported. Such methods also build the theoretical basis of the second research period. 

# 3.4.1.2. The research limitation

Due to the technical and material constraints, there are some limitations of the research during this period, which can be summarized as follows: 

 To neglect the winding factors besides the working harmonic is valid for the case of fundamental harmonic winding topology. This is not the case for over-harmonic winding topology, since the subharmonics may strongly impact the machine performance (chapter 2). With the classical design methods and the resulting classical winding topology, it is not possible to reduce the sub-harmonics contents suciently. New winding topology and new design methods need to be further investigated. 

 All the winding topology considered during this research period is named as classical winding topology, which is the single- or doublelayer winding with coils of the same number of turns and coil pitch. More complicated topology is considered as unpractical. Nevertheless, ideas about winding with a dierent number of conductors per each slot [69] and winding with coils of dierent coil pitch and number of turns [61] were introduced. Especially for over-harmonic winding such more complicated winding topology performs better electromagnetic property and can be manufactured without di- culty nowadays. 

# 3.4.2. The treatment of over-harmonic winding topology since the 1980s

The second research period in the eld of winding topology treatment begins with the invention of high energy neodymium permanent magnet by M. Sagawa [44], which makes the air-gap ux density of a permanent magnet synchronous machine for the rst time competitive with an electrically excited synchronous machine or an induction motor. The great advantage of the permanent magnet synchronous machine is that the air-gap ux density caused by the permanent magnet from the rotor is almost independent of the number of rotor poles (6). This makes it possible to design a permanent magnet synchronous machine with overharmonic winding topology, where the air-gap torque density is comparable to its counterpart with fundamental harmonic winding topology (7). It is quickly recognized that by using permanent magnet synchronous machine with over-harmonic winding topology, a thinner back iron yoke is possible. This leads to an increasing of the air-gap diameter and therefore a higher torque density $( T _ { q } \sim \frac { 1 } { 2 } D _ { \delta } \cdot \overline { { { f } } } )$ for a given design space. Moreover, the over-harmonic winding can be realized by using coils with coil pitch equal to single slot pitch, which is with the advantage of short and no overlapping end-winding, higher slot lling factor, easy to production. Therefore, the research interest is focused on the analysis and design of over-harmonic winding. 

Another driver for this research period is the rapid development of the power electronics, which makes it easy to use a multi-phase current source. Multi-phase winding topology as an alternative to its 3-phase counterpart attracts more and more attentions 

The rapid increasing of the computing power of the modern computer and the progress in the computer technique also bring new impulse into the eld of winding topology treatment. Analysis and design methods based on algorithmic approach are more preferred as the graphical methods as the tools of the engineer are computer and software, no paper and pencil anymore. 

A comprehensive research of the publications leads to the following summary of the research activity, which is still very active and far from completed. 

# 3.4.2.1. The adaptation of the long standing methods for over-harmonic winding topology

Winding topology design In the eld of winding topology design, three main research activities can be observed: 

 Adaption of the general design methods for the special case of overharmonic winding topology. Eorts are made both for the star of slots method [2, 9] and the Kauders' systematic [13, 36]. With the aid of the digital computer, the drawback of the Kauder's systematic is overcame, and for the special case of winding with coils of coil pitch equal to single slot pitch, this method can be strongly simplied. All this makes the Kauders' systematic more and more attractive. 

 A great eorts are made to integrate the winding design method into electrical machine design procedure. This is because the winding topology of the electrical machine should be known before the electromagnetic eld calculation starts. For the implementation are the method of R. Richter [66, 75, 74, 76, 39] as well as the method of W. Kauders [37, 36] used. After the winding topology design, the subsequent eld calculation occurs either with analytical [39] or with nite element analysis [37, 66]. Thus the impacts of the winding topology on the machine performance, such as inductance, back EMF, electromagnetic torque, etc. are predicted. 

 New ideas about winding topology design are introduced by exploiting the progress of the mathematics and computer technique. The winding topology design problem is discrete and nonlinear in nature, which can be considered as a mathematical optimization problem with constraints. The computer-aided stochastic algorithm, such as genetic algorithm, is introduced to solve this problem through optimizing multiple objectives [47, 8, 65, 7]. All these methods have the same point in common: not only the winding factor of the working harmonic but also the sub- and over-harmonics are considered simultaneously. This is necessary for the over-harmonic winding topology but makes the optimization more complicate. 

Winding topology modication To reduce the sub-harmonic contents a great number of investigation are done, which is to modify the well-known classical winding topology obtained through the classical winding topology design method. Dierent winding topology modication approaches are introduced: the multi-layer approach [23, 2, 45] by increasing the number of layers (till max. 4 layers), the multi-slot approach [19, 56, 57] by doubling the number of slot and inserting one more set of winding, the multi-turn approach [18, 17, 42, 19, 78] by using coils of dierent number of turns and the multi-conductor approach [20] by using coil with dierent number of conductors per coil side. The modication is generally based on heuristic approach. 

Winding topology analysis All the classical winding topology of fundamental and over-harmonic can be suciently solved by the star of slots method. This is not the case for a winding topology where each slot is with a dierent number of conductors. This problem is systematically analyzed by R. Cipin et al. [16, 15], where the Fourier analysis of the socall conductor density function of one single-phase winding is used. The winding factor is then calculated through the Fourier coecients. Two types of conductor density function are investigated: conductor density function as Dirac delta function in the middle of the slot and conductor density function as rectangular function over the slot pitch. 

# 3.4.2.2. The research limitations

Great success is also achieved during this research period. Especially the introduction of permanent magnet synchronous machine with overharmonic winding gives this age-old topic new opportunities and challenges and leads to new ideas and developments. A comprehensive overview is given by El-Refaie in [26, 25]. 

Nevertheless, from the theoretical and methodical point of view, the research limitations can be summarized as follows: 

 The main research work lies in the adoption and implementation of the well-established methods. 

 The winding topology modication methods are heuristic and problem dependent. 

 The optimization algorithm used for winding topology design is stochastic and inecient. Thus no global optimum is guaranteed. 

The development of a physics-based, simple, ecient, deterministic and unied method is thus considered as the challenge of this thesis. 

# 4. A systematical classication of winding topology treatment methods

# 4.1. Preamble

In this Chapter, it is tried to give a systematical classication of the methods for winding topology treatment. This is based on the following considerations: 

 Although most of the classical winding design and analysis methods can be found in the classic book written by H. Sequenz [63], two important works were not done by him. First, H. Sequenz didn't give a clear and structured overview of the methods. As a result, dierent methods appear in dierent place of his book, and this makes the reader quickly lose the overview of this topic by reading his book. Second, H. Sequenz didn't point out the dierence and relationship between the various methods. In his book, he had described only the principle of dierent methods and focused on showing how to use dierent methods to analyze and design winding topology (through a lot of examples). This approach makes the reader learn and understand a particular method easily. At the same time, such approach prohibits the reader to understand all the methods and to obtain the theoretical background of the methods. Because the reader may understand that dierent methods are based on dierent theoretical bases, and they should be individually treated. In reality, all the winding methods are based on the same theoretical consideration, and there is only mirror dierence between them. 

The rst purpose of this chapter is to nish the work not done by H. Sequenz. If this is done, the reader can obtain a more structured overview of this topic which should help the reader better to understand and to do the research on this topic. 

 As mentioned in the previous chapter, there are new developments of winding topology treatment methods after the publication of the classic book by H. Sequenz: the introduction of computer-aided methods to design winding topology and the introduction of winding topology modication methods to achieve particular features. Therefore, the classical winding topology treatment methods should be extended, and the relationship between the new and classical methods should be outlined. Furthermore, the new methods should be put into the same theoretical framework. 

The second purpose of this chapter is to outline the relationship between the new and classical methods and to extend the theoretical framework so that the new methods can be placed in the same theoretical framework. 

 Because this thesis aims at introducing a unied method for winding topology treatment, it should be necessary to show that if a winding topology can be obtained using the methods proposed in this chapter, the same result or an even better result can be obtained by using the introduced method. It will be shown later that most of the winding topologies obtained in this chapter can be derived from the introduced method by introducing dierent design constraints. Therefore, it is reasonable to name the introduced method a unied method. 

Based on the considerations above, an overview of the methods for winding topology treatment is given in gure 4.1. Each particular method would be discussed in the remaining parts of this chapter in detail. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/899c5725a571c363563ed72bf0cd3ce176992213a511eb119f31f309e67b3afb.jpg)



Figure 4. 1 . : Methods for winding topology treatment : the theoretical framework


# 4.2. Winding topology analysis methods

For a better understanding of the particular method, two well-known examples of 3-phase double-layer winding with 12 slots are investigated. The rst example is with the fundamental harmonic as the working harmonic (gure 4.2a) and the second example is with the 5-harmonic as the working harmonic (gure 4.2b). 

In the illustrations, the indices outside the stator contour are used to give the information about the corresponding slot position. For a clearer illustration, the 3-phase winding is illustrated with three gures with dierent colors. Each gure and color indicate one particular phase winding. Two symbols } and  are used to indicate the positive and negative winding direction of the coil sides of a coil respectively. The positive and negative coil sides are connected with a bold dark line, indicating an along the stator circumference distributed coil. In order to give the information about the number of turns of a particular coil, a number surrounded by a lime circle and pointing to the particular coil with a red line is denoted. For the winding topologies given in Figure 4.2, all the coils are assumed with the same number of turns $( w _ { c } = 1 )$ . 

According to dierent points of view, the winding topology analysis methods can be classied into two main categories. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/572fb14080f42f20c01af861d1db3a2efcbbbaede4e7bbc02b78d702f0a496e7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/c419df6c0d3c6e2a9ec4e780eab76d869203e4d230dcf1704577899b12f93f46.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/accb5a251d39ff3a4284cc27fa9186fbc7eb8b7240d92f1f7352a47777d35625.jpg)



(a) The fundamental harmonic as working harmonic


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/1e473b711658f9233d2a71b1dd72fc11bc85e31ec4790cce24fa98c46fa6569a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/c4b0a958a45170ab7ec569923387f40395bbf661b54d1a188f11e344a5430ebb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/b345445b6002c896014fe198255ee55dd92dfdca445e09d6cb3548ab3fff77c0.jpg)



(b) The 5-harmonic as working harmonic


Figure 4. 2 . : The investigated winding topologies 

# 4.2.1. Methods based on EMF analysis

The idea of this type of methods is to assume that there are sinusoidal ux density space harmonics of dierent harmonic orders acting on the conductors of the winding: 

$$
B (x, t) = \operatorname{Re} \left\{\sum_ {\nu = - \infty} ^ {\infty} \hat {B} _ {\nu} \mathrm{e} ^ {j (\omega t + \nu \frac {2 \pi}{l _ {c}} x)} \right\} \tag {4.1}
$$

where $l _ { c }$ is the circumference of the machine. 

For one conductor at position $x _ { n }$ , the induced voltage is: 

$$
u _ {n} (t) = B (x _ {n}, t) l _ {z} v = \mathrm{Re} \left\{\sum_ {\nu = - \infty} ^ {\infty} \hat {u} _ {\nu} \mathrm{e} ^ {j (\omega t + \phi_ {x _ {n}, \nu})} \right\} \tag {4.2}
$$

with 

$$
\hat {u} _ {\nu} = v _ {\nu} l _ {z} \hat {B} _ {\nu}, \phi_ {\nu} = \nu \frac {2 \pi}{l _ {c}} x _ {n}
$$

where $l _ { z }$ is the axial length of the machine and $v _ { \nu }$ is the velocity of the ν-th harmonic. 

For each harmonic order, conductors at dierent positions are so that with induced voltage of equal amplitude but dierent phases. Since each phase winding is seen as a connection of the conductors, the induced voltage of a phase winding is obtained by the sum of the induced voltage of the conductors. 

Based on whether the internal structure of the winding topology is considered, there are two main types of methods with this category. 

# 4.2.1.1. The composite Approach

For the composite approach, only the total winding factor is of interest. The primary objective of such approach is the electromagnetic property of the winding topology. It can be seen as to apply the star of slots method for winding topology analysis. 

The composite approach involves the following steps: 

1. From the winding schema, identify the conductors belonging to the same phase winding and nd out the slot position and the winding direction of each conductor. 

All this information can be compactly formulated by using a vector w, where the winding direction can be obtained through sign (w) and the slot position can be obtained through abs (w). 

The investigated fundamental harmonic winding topology (gure 4.2a) is then formulated as: 

$$
\boldsymbol {w} _ {1} = \left[ \begin{array}{c c c c c c c c} + 1 & - 4 & - 5 & - 5 & - 6 & + 1 1 & + 1 2 & + 1 2 \end{array} \right]
$$

and the investigated over-harmonic winding topology (gure 4.2b) is given by: 

$$
\pmb {w} _ {5} = \left[ \begin{array}{l l l l l l l l} + 1 & - 4 & + 5 & + 5 & - 6 & + 1 1 & - 1 2 & - 1 2 \end{array} \right]
$$

2. Calculate the EMF phasor of each conductor for a particular harmonic order ν by considering the position of each conductor: 

$$
\underline {{\boldsymbol {u}}} = \mathrm{e} ^ {j \nu \frac {2 \pi}{N _ {s}} \operatorname{abs} (\boldsymbol {w})} \tag {4.3}
$$

3. Sum up the conductor EMF phasors for one phase by considering the winding direction of each conductor: 

$$
\underline {{u}} = \sum \operatorname{sign} (\boldsymbol {w}) \cdot \underline {{\boldsymbol {u}}} \tag {4.4}
$$

4. Calculate the winding factor by normalizing the phase EMF phasor to the total number of conductors : 

$$
\xi_ {\nu} = \frac {\mathrm{abs} (\underline {{u}})}{\mathrm{size} (\underline {{u}})} \tag {4.5}
$$

where the function abs(x) returns the absolute value of each element in $\pmb { x } ^ { ( 1 ) }$ , the function sign(x) returns the sign of each element in x and the function size(x) returns the number of elements in x. 

Such approach is simple to understand, easy to implement and leads fast to the winding factor harmonic spectrum. For the winding topologies given in gure 4.2, the calculated winding factor harmonic spectrum are given in gure 4.3. Two eects can be observed from the obtained results: 

 The winding factor harmonic spectrum is the same for both negative and positive harmonic orders. This is because the analysis considers only one single-phase winding. 

 The period of the winding factor harmonic spectrum is the same as the number of slots $N _ { s }$ . This periodicity can be seen from equation 4.3. 

The drawback of such approach is that it does not provide information about how the internal structure of the winding topology aects the total winding factor of dierent harmonic order. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/0d23ab9f6ca3cd3bebf59aae3c3f8a58ffcebf7dc8435d8abdd25750969be136.jpg)



(a) For the fundamental winding topology


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/74f6b92a09aa1eb090d5dcff6191adaa10b5ad960872f643c8c8b072b1cf0652.jpg)



harmonic



(b) For the over-harmonic winding topology



Figure 4.3.: The winding factor harmonic spectrum of the winding topology given in gure 4.2, calculated by using the composite approach


# 4.2.1.2. The de-composite approach

Unlike the composite approach, which calculates the total winding factor without considering the internal winding structure, the de-composite approach treats the winding topology as a hierarchically constructed structure and calculates the total winding factor as a product of the particular partial winding factors. Such approach can be seen as the application of the Kauders' systematics for winding topology analysis (2). 

In order to analyze the winding topology, the rst step is to separate each phase winding into two parts, which are termed as positive and negative winding zones. Within each winding zone, all the coils are with the same winding direction. Each winding zone can be further separated into the so-called coil groups which are connected in series. Each coil group is considered as a series connection of coils. 

An corresponding illustration of the rst phase winding given in gure 4.2b is shown in gure 4.4. The rst sub-gure illustrates the positive and negative winding zones. The second sub-gure illustrates the coil group of the positive winding zone and the third sub-gure illustrates the coil. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/81e1cb671b7785fd497bbf856bd0189bd43015830462cf69dcf18d5c7f7ff0f6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/4587f4babe0c0c6c90a595c2bba86ac96ed6dde0cbb110c550e4d50d0459f220.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/6b55c4336401e3a1ca450cae00b573bb2642462966c8e16c45310e07d703f919.jpg)



Figure 4.4.: The hierarchical structure of the phase winding given in - gure 4.2b


If all the coils are having the same coil pitch and number of turns, all the coil groups are having the same number of coils which are connected in the same way, and the distance between adjacent coil group is the same. Then the particular partial winding factor of the winding topology can be calculated through the following equations: 

1. Winding factor for the coils. The coil pitch is considered as x slot pitch (3): 

$$
\xi_ {\nu} ^ {\mathrm{I}} = \sin (\alpha_ {\nu} ^ {\mathrm{I}}) \tag {4.6}
$$

$\begin{array} { r } { \mathrm { w i t h \ } \alpha _ { \nu } ^ { \mathrm { I } } = \frac { 1 } { 2 } \nu \frac { 2 \pi } { N _ { s } } x . } \end{array}$ 

For the fundamental harmonic winding topology (gure 4.2a) is x = 5 and for the over-harmonic winding topology (gure 4.2b) is x = 1. 

2. Winding factor for the coil group. The coil group is a series connection of b coils of the same winding direction. The distance between adjacent coils is given as f which is obtained by counting the number of slots between the adjacent coils. This leads to: 

$$
\xi_ {\nu} ^ {\mathrm{II}} = \frac {\sin (b \alpha_ {\nu} ^ {\mathrm{II}})}{b \sin (\alpha_ {\nu} ^ {\mathrm{II}})} \tag {4.7}
$$

with $\begin{array} { r } { \alpha ^ { \mathrm { I I } } = \frac { 1 } { 2 } \nu \frac { 2 \pi } { N _ { s } } f . } \end{array}$ 

For the investigated fundamental harmonic winding topology (- gure 4.2a) is $f = 1$ and for the over-harmonic winding topology (gure 4.2b) is f = 5. For both cases is b = 2. 

It is to mention that for the special case $\alpha ^ { \mathrm { I I } } = 0$ , equation 4.7 changes to: 

$$
\xi_ {\nu} ^ {\mathrm{II}} = \frac {b \alpha_ {\nu} ^ {\mathrm{II}}}{b \alpha_ {\nu} ^ {\mathrm{II}}} = 1 \tag {4.8}
$$

since $\begin{array} { r } { \operatorname* { l i m } _ { \alpha _ { \nu } ^ { \mathrm { I I } } \to 0 } \sin ( \alpha _ { \nu } ^ { \mathrm { I I } } ) = \alpha _ { \nu } ^ { \mathrm { I I } } } \end{array}$ . 

3. Angle oset of adjacent coil groups. The distance between the adjacent coil groups is considered as y which is measured by counting the number of coil groups between adjacent coil groups (gure 4.5). 

$$
\alpha_ {\nu} ^ {\mathrm{III}} = \frac {1}{2} \nu \frac {2 \pi}{K} y \tag {4.9}
$$

where K is the total number of coil groups of the multi-phase winding topology. 

Since for the both investigated winding topologies, there is just one coil group within each winding zone, and this leads to $y = 0$ and $\alpha _ { \nu } ^ { \mathrm { I I I } } = 0$ . 

4. Winding factor for the winding zone. It is to assume that within the positive winding zone there are $Z _ { 1 }$ coil groups and within the negative winding zone there are $Z _ { 2 }$ coil groups: 

$$
\xi_ {\nu} ^ {\mathrm{IV}} = \frac {\sqrt {\sin^ {2} (Z _ {1} \alpha_ {\nu} ^ {\mathrm{III}}) + \sin^ {2} (Z _ {2} \alpha_ {\nu} ^ {\mathrm{III}}) - 2 \sin (Z _ {1} \alpha_ {\nu} ^ {\mathrm{III}}) \sin (Z _ {2} \alpha_ {\nu} ^ {\mathrm{III}}) \cos (\alpha_ {\nu} ^ {\mathrm{IV}})}}{(Z _ {1} + Z _ {2}) \sin (\alpha_ {\nu} ^ {\mathrm{III}})} \tag {4.10}
$$

where $\begin{array} { r } { \alpha _ { \nu } ^ { \mathrm { I V } } = \nu \frac { 2 \pi } { K } \frac { K } { 2 } } \end{array}$ . Depends on weather the harmonic order ν is odd or even, the term cos $( \alpha _ { \nu } ^ { \mathrm { I V } } ) = \pm 1$ , . 

It is to mention that for the special case $\alpha _ { \nu } ^ { \mathrm { I I I } } = 0$ , equation 4.10 changes to: 

$$
\xi_ {\nu} ^ {\mathrm{IV}} = \frac {\sqrt {(Z _ {1}) ^ {2} + (Z _ {2}) ^ {2} - 2 Z _ {1} Z _ {2} \cos (\alpha_ {\nu} ^ {\mathrm{IV}})}}{Z _ {1} + Z _ {2}} \tag {4.11}
$$

since $\mathrm { l i m } _ { \alpha _ { \nu } ^ { \mathrm { I I I } }  0 } \sin ( \alpha _ { \nu } ^ { \mathrm { I I I } } ) = \alpha _ { \nu } ^ { \mathrm { I I I } }$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/1b93d583fabb15891f1c2f9eda35e0e0c09320775e8962971430a24e35c9efd8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/74695e2cab973d9471aabf552595b9d539b0d3a9260f0de4be77d3c528750e59.jpg)



(a) The total 6 coil groups of a multiphase winding.Each coil group is consist of two coils and is indicated with one particular color.



(b) The rst and third coil groups of the multi-phase winding given in the left side. The distance between the two coil groups is $y = 2$


Figure 4.5.: Illustration of the distance between coil groups 

Once the winding factor of each winding structure is known, the total winding factor can be obtained: 

$$
\xi_ {\nu} = \xi_ {\nu} ^ {\mathrm{I}} \cdot \xi_ {\nu} ^ {\mathrm{II}} \cdot \xi_ {\nu} ^ {\mathrm{IV}} \tag {4.12}
$$

where the rst winding factor $\xi _ { \nu } ^ { \mathrm { I } }$ is named as chording factor which considers the impacts of the coil width on the total winding factor, the second winding factor $\xi _ { \nu } ^ { \mathrm { I I } }$ is named as group factor which considers the impacts of the distribution of the coils within one coil group on the total winding factor. The third winding factor $\xi _ { \nu } ^ { \mathrm { I V } }$ is rarely mentioned in the textbook, since for the most cases, the coil group within the positive and negative winding zone are the same $Z _ { 1 } = Z _ { 2 }$ . For this special case, $\xi _ { \nu } ^ { \mathrm { I V } } = \bar { \{ 0 , 1 \} }$ , depending on weather the harmonic order ν is odd or even. 

The partial and total winding factors for the investigated fundamental and over-harmonic winding topology are given in gure 4.6. For the partial and total winding factor harmonic spectrum, it is observed that the winding factor harmonic spectrum is the same for positive and negative harmonic orders and the winding factor harmonic spectrum is with a period equal to the number of slot $N _ { s }$ . When compared with the winding factor harmonic spectrum calculated with the composite approach in the previous section (gure 4.3), the results of the both methods yield the same harmonic spectrum for the total winding factor. 

The advantage of this approach is that a detailed knowledge of how each winding structure aects the winding factor spectrum can be obtained and thus it makes a better understanding of the winding structure. The major drawback of this approach is that the mapping between the characteristic numbers and the winding topology is not unique. This means the same winding topology can be represented by using dierent sets of characteristic numbers. 

In order to illustrate this problem, the over-harmonic winding is used (gure 4.2a). The winding can be seen either as: within each winding zone, there is one coil group and each coil group is with two coils, this leads to $b = 2 , f = 5 , K = 6 , y = 0 , Z _ { 1 } = 1 , Z _ { 2 } = 1$ or as: within each winding zone, there is two coil groups and each coil group is with one coil, this leads to $b = 1 , f = 0 , y = 5 , K = 1 2 , Z _ { 1 } = 2 , Z _ { 2 } = 2$ . Although both the results lead to the same total winding factor harmonic spectrum, the harmonic spectrum of the particular partial winding factors are quite dierent (gure 4.7). Such non-unique mapping makes the analysis quite confusing. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/187681d89785f3bc1eaeff174caa61a598258477124e7ecd28bd4644e06e546b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/be2c7b8c4b524657b6f0682463430ea959f2d2ba618ac29de9b6a89f4fe3a992.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/64c59f19033fdb9a2ed87efff087ee4a4f74e8aba2c088f5f01932a26062bcd5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2816def336d4cb15996f1e42a6011f2afdd53f516811e46fc9c14bdd107ed508.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/9026e6995614497c92d9f5ceb8944c1306ae39d732e0997295b0480a5240ae0c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/9f335c0e6af995309bcfd387f61f1213e0f881ff4d0d26201feec6251bc3db9b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/ebaaf11eb773dbd15c7a06ec81aaf7082ff28542205fc5fe3972c9e303534c66.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/ea6b359a15c2f7c027345c86f87a6d636dc645c1a0e603279b4d4b45786fb606.jpg)



(a) For the fundamental harmonic winding topology



(b) For the over-harmonic winding topology



Figure 4.6.: The winding factor harmonic spectrum for the winding topologies given in gure 4.2 calculated by using the de-composite approach


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/d0b348c52f4c4e9407f0fe9729d53554eb731c9fb08d8e6f30591d995d4e485a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/96dd5db7fcd1df98956a5a5d69a1abf3964ea6f3de76bc9d499a37d07193489b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/8cf463dff8bb4c3b7a8c2c3a0f568ad8b93e33f6a76cb2c0c87549326672e2d7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/94365aa6c0714f34a16c9510fce924cfa13e19e25c3af4a2e7c7a99290a11ee3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/106947ccd19a2b5123ff0f046989c20d5fb84a2dcc6da9e8de23d5ed40be4d1e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/0104d1999eeabb84cc9b533f72a70391500f13b52ce820eb72bab623db7ba4c1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/634c50a14321f062e422a9a385ad7cc0eba7ff1e32e2ff3c2ca18dbf19ef17c8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/1544652d2fbce636ede05ef15aa881baf0b778c9972df1514061b5bc86179402.jpg)



(a) b = 2, f = 5, K = 6, y = 0, Z1 = (b) b = 1, f = 0, y = 5, K = 12, Z1 = 1, Z = 1 2, Z = 2


Figure 4.7.: The winding factor harmonic spectrum of the over-harmonic winding calculated by using dierent characteristic parameters 

# 4.2.2. Methods based on MMF analysis

The idea of this type of methods is to assume that the spatial MMF distribution can be seen as several sinusoidal MMF space harmonics of dierent harmonic orders. The Fourier analysis of the MMF space distribution is used to get the sinusoidal MMF space harmonic of particular harmonic order. 

The MMF distribution of the multi-phase winding is considered as $\Theta ( x , t )$ which is a superposition of the MMF distribution of each phase winding $\Theta _ { k } ( x , t )$ . The MMF distribution of each phase winding is dened as the number of conductors times the phase current by considering the winding direction of the conductors. Based on these considerations, the MMF distribution of the multi-phase winding can be formulated as: 

$$
\Theta (x, t) = \mathrm{Re} \left\{\sum_ {k = 1} ^ {m} N _ {c, k} (x) \cdot O _ {c, k} (x) \cdot \hat {i} \mathrm{e} ^ {j (\omega t + \phi_ {k})} \right\} \tag {4.13}
$$

where $N _ { c , k } ( x )$ is the number of conductors belonging to phase k at position $x , O _ { c , k } ( x )$ characterizes the winding direction of the conductors and $\hat { i } , \omega$ are the amplitude and frequency of the phase current. 

By using the space harmonic description, $\Theta ( x , t )$ can be formulated as: 

$$
\Theta (x, t) = \mathrm{Re} \left\{\sum_ {\nu = - \infty} ^ {+ \infty} \underline {{C}} _ {\nu} (t) \mathrm{e} ^ {j \nu \frac {2 \pi}{l _ {c}} x} \right\} \tag {4.14}
$$

where $\nu$ is the space harmonic order, x is the space coordinate and $l _ { c }$ is the circumference of the machine. The coecient $\underline { { C } } _ { \nu } ( t )$ can be seen as the superposition of each phase winding: 

$$
\begin{array}{l} \underline {{C}} _ {\nu} (t) = \underline {{C}} _ {\nu} \mathrm{e} ^ {j \omega t} \\ = \sum_ {k = 1} ^ {m} \underline {{C}} _ {k, \nu} \mathrm{e} ^ {j \omega t} \tag {4.15} \\ \end{array}
$$

where the Fourier coecient of each phase $\underline { { C } } _ { k , \nu }$ is determined through the Fourier analysis: 

$$
\underline {{C}} _ {k, \nu} = \frac {1}{l _ {c}} \int_ {0} ^ {l _ {c}} N _ {c, k} (x) \cdot O _ {c, k} (x) \cdot \mathrm{e} ^ {- j \nu \frac {2 \pi}{l _ {c}} x} \mathrm{d} x \cdot \hat {i} \mathrm{e} ^ {j \phi_ {k}} \tag {4.16}
$$

The winding factor $\xi _ { \nu }$ can be interpreted as the normalization of the Fourier coecient $\underline { { C } } _ { \nu }$ : 

$$
\xi_ {\nu} (t) = \frac {| \underline {{C}} _ {\nu} |}{C _ {\nu}} \tag {4.17}
$$

which should be $\xi _ { \nu } \ \leq \ 1$ . Thus a reasonable denominator $C _ { \nu }$ can be chosen as: 

$$
C _ {\nu} = \frac {1}{l _ {c}} \sum_ {k = 1} ^ {m} N _ {c, k} \cdot \hat {i} \tag {4.18}
$$

since it is always 

$$
| O _ {c, k} (x) \cdot \mathrm{e} ^ {- j \nu \frac {2 \pi}{l _ {c}} x} \cdot \mathrm{e} ^ {j (\omega t + \phi_ {k})} | \leq 1
$$

and 

$$
N _ {c, k} = \int_ {0} ^ {l _ {c}} N _ {c, k} (x) \mathrm{d} x
$$

Due to the normalization, the winding factor is independent of the amplitude of the phase current and the circumference of the machine. Therefore, $\hat { i } = 1$ and ${ l _ { c } = 1 }$ are used for further consideration. 

Based on the assumption in the MMF function $\Theta ( x )$ , the methods can be sorted into two groups. The rst group of methods is based on dierent assumptions about the MMF function domain and the second group of methods is based on dierent assumptions about the shape of the MMF function. 

# 4.2.2.1. Analysis of the MMF function of dierent domain

MMF of one phase winding In this approach, only the MMF of one phase winding is considered for the Fourier analysis. The resulting winding factor spectrum is then used to represent the multi-phase winding. This is only valid for each phase winding having the same topology, which is always assumed as the precondition of the symmetrical multiphase winding. 

Under this assumption, the winding factor is time independent, since the length of the phasor $\underline { { C } } _ { k , \nu }$ is time independent: 

$$
\xi_ {\nu} = \xi_ {k, \nu} = \frac {| \underline {{C}} _ {k , \nu} |}{C _ {k , \nu}} \tag {4.19}
$$

MMF of the multi-phase winding In this approach, the MMF function of the multi-phase winding is used for the Fourier analysis. The advantage of such approach is that it is valid for both symmetrical and asymmetrical winding topology. Furthermore, it provides the possibility to verify if the symmetry condition of the analyzed winding matches both in space and time (4). Non-matched symmetry in space and time leads to: 

$$
\underline {{C}} _ {\nu} = 0 \tag {4.20}
$$

# 4.2.2.2. Analysis of the MMF function of dierent shape

MMF as Dirac delta function in the slot middle Such approach can be found in [16, 15], where the MMF function is assumed as: 

$$
N _ {c, k} (x) = N _ {c, k, n} \cdot O _ {c, k, n} \cdot \delta (x - x _ {k, n}) \tag {4.21}
$$

which simplies the expression of $\underline { { C } } _ { k , \nu }$ to: 

$$
\underline {{C}} _ {k, \nu} = \sum_ {n = 1} ^ {N _ {s}} N _ {c, k, n} \cdot O _ {c, k, n} \cdot \mathrm{e} ^ {- j \nu \frac {2 \pi}{l _ {c}} x _ {k, n}} \tag {4.22}
$$

By using the vector notation, a compact form of the Fourier coecients can be obtained: 

$$
\underline {{C}} _ {k, \nu} = \mathrm{sum} \left(\boldsymbol {N} _ {c, k} \cdot \boldsymbol {O} _ {c, k} \cdot \mathrm{e} ^ {- j \nu \frac {2 \pi}{l _ {c}} \boldsymbol {x} _ {k}}\right) \tag {4.23}
$$

The investigated fundamental harmonic winding topology is then expressed as: 

$$
\begin{array}{l} \boldsymbol {N} _ {c, 0} = \left[ \begin{array}{c c c c c c} 1 & 1 & 2 & 1 & 1 & 2 \end{array} \right] \\ \boldsymbol {O} _ {c, 0} = \left[ \begin{array}{c c c c c c} + 1 & - 1 & - 1 & - 1 & + 1 & + 1 \end{array} \right] \\ \boldsymbol {x} _ {c, 0} = \left[ \begin{array}{c c c c c c} 1 & 4 & 5 & 6 & 1 1 & 1 2 \end{array} \right] \\ \end{array}
$$

while for the over-harmonic winding topology, there is: 

$$
\begin{array}{l} \boldsymbol {N} _ {c, 0} = \left[ \begin{array}{c c c c c c} 1 & 1 & 2 & 1 & 1 & 2 \end{array} \right] \\ \boldsymbol {O} _ {c, 0} = \left[ \begin{array}{c c c c c c} + 1 & - 1 & + 1 & + 1 & - 1 & - 1 \end{array} \right] \\ \boldsymbol {x} _ {c, 0} = \left[ \begin{array}{c c c c c c} 1 & 4 & 5 & 6 & 1 1 & 1 2 \end{array} \right] \\ \end{array}
$$

A comparison of equation 4.4 and 4.22 shows that equation 4.3 is a special case of equation 4.22 where the number of conductors $N _ { c , k , n }$ of each phase and each slot are the same: $N _ { c , k , n } = \mathrm { c o n s t } .$ .. 

MMF as rectangle-shaped function over the slot opening Under this assumption, the MMF function can be formulated as: 

$$
N _ {c, k} (x) = N _ {c, k, n} \cdot O _ {c, k, n} \cdot \operatorname{rect} \left(\frac {x - x _ {k , n}}{\tau_ {s o}}\right) \tag {4.24}
$$

where $\tau _ { s o }$ is the width of the slot opening. This leads to the following expression for $\underline { { C _ { k , \nu } ^ { \prime } } } \mathrm { : }$ : 

$$
\underline {{C}} _ {k, \nu} ^ {\prime} = \frac {\sin \left(\pi \frac {\nu}{l _ {c}} \tau_ {s o}\right)}{\pi \frac {\nu}{l _ {c}} \tau_ {s o}} \underline {{C}} _ {k, \nu} \tag {4.25}
$$

Since the coecient $C _ { \nu }$ (equation 4.18) is independent on the shape of the MMF function, the winding factor for such shape of MMF function is: 

$$
\xi_ {\nu} ^ {\prime} = \frac {\sin \left(\pi \frac {\nu}{l _ {c}} \tau_ {s o}\right)}{\pi \frac {\nu}{l _ {c}} \tau_ {s o}} \xi_ {\nu} \tag {4.26}
$$

which is dependent on the slot opening $\tau _ { s o }$ . 

MMF as rectangle-shaped function over the slot pitch such approach can be found in [16, 15]. There is just a minor dierence between this approach and the approach above. Instead of using the slot opening $\tau _ { s o }$ , the slot pitch $\tau _ { s p }$ is used in the equation: 

$$
N _ {c, k} (x) = N _ {c, k, n} \cdot N _ {c, k, n} \cdot \operatorname{rect} \left(\frac {x - x _ {k , n}}{\tau_ {s p}}\right) \tag {4.27}
$$

This leads to a slot pitch $\tau _ { s p }$ dependent winding factor: 

$$
\xi_ {\nu} ^ {\prime \prime} = \frac {\sin \left(\pi \frac {\nu}{l _ {c}} \tau_ {s p}\right)}{\pi \frac {\nu}{l _ {c}} \tau_ {s p}} \xi_ {\nu} \tag {4.28}
$$

For the winding topology analysis, it is better to let the geometrical dimension of the machine outside the consideration, and thus the analysis focuses only on the topological property of the winding. From this point of view, it is more reasonable to assume the MMF as Dirac delta function. Furthermore, the method under this assumption can be seen as an extension of the star of slots method for the general cases. It is therefore recommended to use equation 4.23 for the calculation of the winding factor harmonic spectrum. 

The analysis results of the MMF distribution of the fundamental and over-harmonic winding topology are given in gure 4.8. In the top gure, the Fourier analysis is applied to MMF distribution of one phase winding and in the bottom gure, the MMF distribution of the multi-phase winding is Fourier analyzed. The result for MMF distribution assumed as Dirac delta function is shown by the blue bars, the result for MMF distribution assumed as rectangle-shaped function over the slot opening (the slot opening is assumed as 0.5 slot pitch) is shown by the lime bars and the result for MMF distribution assumed as rectangle-shaped function over the slot pitch is shown by the red bars. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/238728228849da3c55f58f98842dba8bc62c12128355fe294553326dbec51bb2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/eb77035439e8ed568671ca2249050a221820e2f675358c187c733701b43947c9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/22fa45076fd61218f956caacb0c58a1175342a11a8b2d023f8e840ff17a913b1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/9e31d44590af7bfbb758d147b2b9d1c68d6366fbff084572a6af00a728b40a4e.jpg)



(a) For the fundamental harmonic winding, top: only one phase winding is considered, bottom: all the phase windings are considered



(b) For the over-harmonic winding, top: only one phase winding is considered, bottom: all the phase windings are considered



Figure 4.8.: The winding factor spectrum calculated by using the MMF analysis. blue: MMF assumed as Dirac delta function, lime: MMF assumed as rectangle-shaped function over the slot opening, red: MMF assumed as rectangle-shaped function over the slot pitch


# 4.3. Winding topology design methods

In general, the winding topology design methods can be classied into two main categories: 

Winding design methods of the rst category start with the given parameters such as pole pairs, number of slots and number of current phases, and give the winding topology after applying the design procedures. The design purpose of such methods is to maximize the winding factor of the working harmonic. Such methods are named as winding topology layout methods in this thesis. 

 The winding design methods of the second category start with a given winding topology (obtained in general by using the winding topology layout methods) and give a modied winding topology after applying the modication procedures. The design purpose of such methods is to minimize the winding factors of the subharmonics because the working harmonic of the treated winding is in general not the fundamental harmonic. Such methods are named as winding topology modication methods in this thesis. 

# 4.3.1. Winding topology layout methods

The methods of this category can be classied into two main types: the deterministic approach and the stochastic approach. Each winding topology layout method is illustrated through two examples which are to design two 3-phase double-layer windings of 12 slots with the fundamental (p = 1) and 5-th harmonic p = 5 as the working harmonic. 

# 4.3.1.1. The deterministic approach

Methods of this type can be further classied into two main types: 

 methods of the rst type are primarily based on the electromagnetic consideration. By considering the phases of the induced EMF of the conductors (or coils), the aliation of the conductors (or coils) to the corresponding current phase is then determined. 

 Methods of the second type are primarily based on the geometrical consideration. By considering some intuitive feasibility and symmetrical conditions, the aliation of the conductors (or coils) to the corresponding current phase is then determined. Because the results obtained by applying such methods are not always useful, such methods are in general combined with the winding analysis methods, so that the electromagnetic property of the obtained winding topology can be evaluated in the second step. 

# Methods based on electromagnetic consideration

All the methods under this category have the same theoretical basis and can be seen as dierent variants of one basic method. Because of the originality(5) and popularity(6), the star of slots method introduced by R. Richter [59] is considered as the basic method. The other methods are seen as dierent deduced forms of the star of slots method. The relationship of the deduced forms to the basic method will be outlined. 

The original star of slots method The star of slots method introduced by R. Richter [59] can be summarized as follows: 

1. Set-up the star of slots. The star of slots is a set of EMF phasors where the phase angle of the n-th phasor is: 

$$
\alpha_ {n} = p \frac {2 \pi}{N _ {s}} n, \quad n = 0... N _ {s} - 1 \tag {4.29}
$$

The star of slot is dependent on the working harmonic of the winding topology. Figure 4.9a and 4.9b show the star of slots for the fundamental and over-harmonic winding topology respectively. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/9d2a14f7ced789387fa195d7eeb114d75402391428d983c6916614770906a8df.jpg)



(a) For the fundamental harmonic winding topology,


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/fcbc345b0345a652f1b7fce5bec4049a8f52c8182de83ce7a25edabfea053ee3.jpg)



(b) For the over-harmonic winding topology,



Figure 4.9.: The working harmonic dependent star of slots for a winding with 12 slots


2. Set-up the sector of the multi-phase current system. The sector span $\Delta \phi$ is dened as: 

$$
\Delta \phi = \frac {\pi}{m} \tag {4.30}
$$

3. Merge the star of slots and the sector of the multi-phase current system. It should be guaranteed that each EMF phasor belongs to a denite sector uniquely. The examples of the fundamental and over-harmonic winding topology are illustrated in gure 4.11. 

4. Set-up the single layer winding topology. This is done by connecting the positive and negative conductors of the same phase to coils. The examples of the fundamental and over-harmonic winding topology are illustrated in gure 4.12. 

5. Obtain the double layer winding topology. This is done by doubling the single layer winding and shifting the second layer for a denite number of slots. The examples of the fundamental and over-harmonic winding topology are illustrated in gure 4.13. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/fc95e375e6ad7cf6d7593ed8d8829a7f5560fef9a2c9370aabedff723486a3be.jpg)



Figure 4.10.: The sector of the 3-phase current system


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/c1d63ff2632617fdc715ce3e1da11b7c96245472bebe03621a9925b9163a011c.jpg)



(a) For the fundamental winding topology


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/641580e1b3843ae65bd66d25aeae9e28da9d72b066c4bfdd0f94354e077a28fc.jpg)



(b) For the over-harmonic winding topology



Figure 4.11.: Merge the star of slots (gure 4.9) and the sector of the 3-phase current system (gure 4.10)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/f67ad3967d65c5f9c09e59f26e3d36e70cdf104f5d8234b64404c487c5da2fad.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/28007ddfaf12dedcea2b1f888b256acea4a7fde3e4514f0615dd8e8634b4abeb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/b17b64331dfff37a6eccca5e79621a29d62468fd95991b58c1fcfabc975ccbab.jpg)



(a) For the fundamental harmonic winding


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/8098705a54f141216b2977de9ca2bb9f9409a86224d3d5893cd36037e088008d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2d1baa76814be1a9b931c0cce51f37006c1f9253734db2ff394c8201b3cdb855.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e94208f626f30422a80a7fe8916d03407e9891ff107e79d210fb7d99124c97ec.jpg)



(b) For the over-harmonic winding


Figure 4. 1 2 . : The single layer winding topology 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e3e01c49f707ea629ac301d7722f7f3982f07226f296bd7ee1270056cbfcd9bd.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/ce6ef78ad8a42ab3e58968b2b90069db7a93eaf53cbd162b60fea3cc83b1ee22.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/fd37092f8c25e5ef3ec79276d91746de2eac73020ca2a2626eb6372f5c5c9f87.jpg)



(a) For the fundamental harmonic winding


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/0ae42d6c8836a1e9c0f558d8c6a0683ab1290103eea12f4eee799c0dfca05885.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/753b9b968757aca252e35f5785ff423f29f30f56f63a3bae99d9448ade89e8e3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2fe6f0de320c61fec532166dd3d5f77b8aee07111e26e64fc479b20172cf1de4.jpg)



(b) For the over-harmonic winding



Figure 4. 13. : The double layer winding topology


The method introduced by E.M. Tingley The method introduced by Tingley [73] is just to use another form to represent the star of slots. Instead of the circular form, a tabular form with an angle of $\frac { 2 \pi } { N _ { s } }$ N between adjacent blocks is used, which is named as Tingley schema 

Deduction of the Tingley schema from the star of slots diagram is given in gure 4.14 for the over-harmonic winding topology as an example. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/646344758763c7529f8df8c2d6250742008ecbb717f5dd397ffbf8b63799643b.jpg)



(a) The star of slots diagram


<table><tr><td></td><td colspan="2">A</td><td colspan="2"><eq>\overline{C}</eq></td><td colspan="2">B</td></tr><tr><td>+</td><td>5</td><td>10</td><td>3</td><td>8</td><td>1</td><td>6</td></tr><tr><td>-</td><td>11</td><td>4</td><td>9</td><td>2</td><td>7</td><td>0</td></tr></table>


(b) The reduced Tingley schema



Figure 4.14.: Deduction of the Tingley schema from the star of slots diagram


The method introduced by V. Bedjanic It is shown above that to set-up the star of slots diagram, R. Richter counts the slot index from 0 to N 1 and calculates the corresponding phasor position (equation 4.29). The method introduced by V. Bedjanic [6] does this in an inverse way. This means that he counts the phasor index from 0 to N 1 and calculates the corresponding slot position. Mathematically, this can be seen as to solve the following equation: 

$$
\mathrm{e} ^ {j p \frac {2 \pi}{N} n _ {k}} = \mathrm{e} ^ {j \frac {2 \pi}{N} k}, \quad k = 0... N - 1 \tag {4.31}
$$

where $n _ { k }$ is seen as unknown. Mathematically, this is equivalent as: to nd out an integer $g _ { k }$ for each k which satises: 

$$
p \cdot n _ {k} = k + N _ {s} \cdot g _ {k}, \quad g _ {k}: \text { integer } \tag {4.32}
$$

The both methods to set-up the star of slots diagram are illustrated in gure 4.15 for the over-harmonic winding topology. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/724c95216392477702a2ad2372cb7a2c955edc6de9135e1762099bfce15253d7.jpg)



Figure 4.15.: Set-up the star of slots diagram by using dierent methods. Top: method introduced by R. Richter, bottom: method introduced by V. Bedjanic


The method introduced by H. Sequenz The method introduced by H. Sequenz is similar to the method introduced by V. Bedjanic. They dier only in the sequence of the design procedure. Instead of counting the phasor index from 0 to $N _ { s } \mathrm { ~ - ~ } 1$ , calculating the corresponding slot index and then considering the phase aliation. H. Sequenz considers rst the positive phasors belonging to the rst phase and calculates the corresponding slot index, then the negative phasors belonging to the same phase and the corresponding slot index. The same procedures are then applied to the other phases. 

Conclusion The idea behind methods of this type can be characterized as from the bottom up approach. This means the design procedure starts from the simplest winding structure and subsequently constructs the more complex structure: from conductors to coils, from coils to singlephase windings, from single-phase windings to multi-phase winding and from single layer winding to double-layer winding. All this is based on the knowledge of the phase aliation of each conductor. To solve the problem of phase aliation of each conductor, the phase of the EMF phasor of the working harmonic is used to assign the conductor to the corresponding current phase. 

The systematical design procedure combined with the physics based consideration makes methods of this type easy to understand and easy to use. Such methods are valid for the design of single and doublelayer winding, fundamental and over-harmonic winding. At the same time, they are suitable to be used as a graphic tool and are easy to be implemented by using high-level computer languages, e.g. C++ or Python. 

Nevertheless, there is a general drawback of this approach. Since the winding topology is based on the simple basic topology, the simple basic topology determines the main property of the winding topology. This means that if some constraints are made for the simple basic topology, then the variations of the resulting winding topology will be strong restricted. Thus a great number of topology is out of consideration. This is especially the case for the over-harmonic winding. This problem is recently recognized, and it is essentially the reason for the research on the winding topology modication methods. 

Another approach to solve this problem is to introduce an inverse design procedure: from the top down approach. Such approach starts with a complex winding topology - in an ideal case the optimal winding topology (in respect of certain criteria) - and simplies it step by step by considering dierent constraints. The unied winding topology design method proposed in this thesis is actually with this approach. Therefore, it xes the drawback without losing the generality. Furthermore, such approach gives more physical insight about the investigated winding topology. 

Methods based on geometric consideration In the category of deterministic methods based on geometrical consideration, the methods can be classied into two types, depending on whether the method is based on a characteristic parameter named number of slots per pole per phase q. It is to mention that such parameter can not be found in the previous methods because it is a pure geometrical parameter, characterizing the geometrical property of the winding topology. 

The Kauders' systematics: a q independent method: The idea of W. Kauders [40, 41] is to introduce necessary and sucient parameters to fully describe the geometrical structure of the winding, which can be directly used to calculate the winding factor. The winding factor is then used as a quantity to characterize the quality of the winding topology. Thus the method contains two major steps: nd the winding topology and then calculate the winding factor for the winding topology. 

By describing the winding structure in a hierarchical and systematical way, as discussed in section 4.2.1.2, the winding structure can be fully characterized by 11 parameters: $Z _ { 1 } , Z _ { 2 } , K , y , p , N _ { s } , b , f , x , N _ { l } , m \ ^ { ( 7 ) }$ , which can be further categorized into four groups. The winding topology is then described as follows: 

 x is used for describing the topology of the coils which is the coil pitch. 

 b and f are used for describing the topology of the coil groups where b is the number of coils within one coil group, and $f$ is the distance of adjacent coils. 

 $y , \ Z _ { 1 }$ and $Z _ { 2 }$ are used for describing the topology of the winding zone where y is the distance between adjacent coil groups, $Z _ { 1 }$ is the number of coil groups within the positive winding zone and $Z _ { 2 }$ is the number of coil groups within the negative winding zone. 

 $N _ { s } , ~ p , ~ N _ { l } ,$ , m and K are used for the describing the topology of the multi-phase winding where $N _ { s }$ is the number of slots, p is the number of pole pairs, $N _ { l }$ is the number of winding layer, m is the number of phases, and K is the number of coil groups. 

By considering the geometrical constraints, following relationships between the parameters can be obtained: 

 Between b, K, $N _ { l }$ and $N _ { l }$ , there is: 

$$
N _ {l} \frac {N _ {s}}{2} = b K
$$

This leads to the determination of the parameter $K$ : 

$$
K = \frac {N _ {l} N _ {s}}{2 b} \tag {4.33}
$$

 Between m, $Z _ { 1 } , Z _ { 2 }$ and K, there is: 

$$
m (Z _ {1} + Z _ {2}) = K
$$

This leads to the determination of the parameter $Z _ { 2 }$ 

$$
Z _ {2} = \frac {K}{m} - Z _ {1} \tag {4.34}
$$

which is based on the assumption that the number of coil groups within each phase winding is the same. 

By considering these geometrical and symmetrical constraints, the number of independent parameters is reduced to $5 ~ ( N _ { s } , p , N _ { l }$ and m are considered as given). The value interval of each independent parameter can be determined based on simple geometrical consideration: 

 For coil pitch x, there is: 

$$
1 \leq x \leq \operatorname{int} \left(\frac {N _ {s}}{2}\right) \tag {4.35}
$$

 For the number of coils b and the distance between adjacent coils $f ,$ there are: 

$$
1 \leq b \leq \frac {N _ {l} N _ {s}}{2 m} \tag {4.36}
$$

$$
0 \leq f \leq \mathrm{int} \left(\frac {N _ {s}}{2}\right)
$$

 For the number of coil groups of the positive winding zone $Z _ { 1 }$ and the distance between adjacent coil groups y, there are: 

$$
1 \leq Z _ {1} \leq \frac {K}{m} \tag {4.37}
$$

$$
0 \leq y \leq \frac {K}{2}
$$

As the relationship between these independent parameters and the winding factor is strongly nonlinear (subsection 4.2.1.2), the determination of these parameters using direct approach is impossible. The only possibility to solve this problem is to use an exhaustion algorithm to check all the possible parameter combinations and nd out the best solution for dened criteria. 

This makes such method useless before the introduction of the digital computer since it is impossible for a human to solve even a simple problem. Recently, this method attracts more and more attention, since the systematical and hierarchical consideration makes it easy to implement with high-level computer languages and it can handle large varieties of winding topology, e.g. single and double layer winding, fundamental and over-harmonic winding, etc. In the thesis done by D. Hülsmann [36] the special case of over-harmonic winding with single tooth coil(8) is treated. 

As an example, the design results of a 3-phase double-layer winding with 12 slots and the 5-th harmonic as working harmonic are given in the gure 4.16. Totally, there are 630 dierent winding topologies available. The winding factor of the working harmonic varies from 0.0173 to 0.9659. It is observed that many designs are with the same winding factor. This is due to the non-unique mapping of the characteristic parameters and the winding topology, which is discussed in subsection 4.2.1.2. Such nonunique mapping makes the method as a winding design method quite inecient. 

The q based Methods Such methods are in general used to treat the special cases of double-layer winding topology where q is considered as a fractional number: 

$$
q = \frac {N _ {s}}{2 m p} = g + \frac {z}{n} \tag {4.38}
$$

where $g , z$ and n are integers. 

The basic idea of such methods is to divide the total $N _ { s }$ coils into z groups of $g + 1$ coils and n groups of g coils and to distribute the z coil groups among the m-phases and $2 p$ poles as symmetrical as possible. A quite simple but loose algorithm is introduced by D. H. Braymer and A. C. Roe [10] for the design of the multi-phase winding topology. A similar approach for the design of the winding topology of one phase is introduced by G. Rebora [54]. Both approaches try to distribute th $\mathrm { ~ \textit ~ { ~ e ~ } ~ } z$ coil groups of the $g + 1$ coils symmetrically among the phases and the poles. If this leads to unreasonable results (e.g. all the coil groups belong to the same phase winding), then they try to do a ne tuning intuitively (9). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a6908d95360f0b2c009b1c674f153518843b1747418dce0da64dd917b88cc49a.jpg)



Figure 4.16.: Design results of a 3-phase double-layer winding with 12 slots and the 5-th harmonic as working harmonic by using the Kauders' method


The method introduced by D. H. Braymer and A. C. Roe is illustrated in gure 4.17 for the case of the 3-phase double-layer winding with 12 slots and the 5-th harmonic as the working harmonic. Totally, there are 30 coil groups, with 12 coil groups of one coil and 18 coil groups without any coil. The distribution of the coil groups among the poles and phases is given on the left of gure 4.17 which leads to the winding topology given in the right. 

A quite complex algorithm is introduced by H. Traÿl [63] for the determination of the distance between the g + 1 coil groups. It can be proved that this is just a mathematical formulation of the statement introduced by D.H. Braymer and A. C. Roe. An extensive analysis of the algorithm shows that with the method introduced by H. Traÿl, the distance between two coil group $x _ { k }$ is guaranteed to oscillate around the non-integer number $n / z { \mathrm { ~ s o ~ } }$ that $\begin{array} { r } { x _ { k } \in \left\{ \mathrm { c e i l } \left( \frac { n } { z } \right) , \mathrm { f l o o r } \left( \frac { n } { z } \right) \right\} } \end{array}$ . This guarantees that the resulting winding topology is as symmetrical as possible. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2ba5a9d476920691868bd322e09f2478b14776c7078ec508217cec593e1a35f3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/722fa7ef89fa62f94e0afc144aa94fa009798fa3e517489dc105f064ab4d8318.jpg)



Figure 4.17.: Illustration of the winding design method introduced by D. H. Braymer and A. C. Roe


# 4.3.1.2. The stochastic approach

Since the winding topology design problem is a strongly non-linear and discontinuous problem with the existence of multiple local minimums, it is mathematically dicult to handle. Genetic multi-objective optimization algorithm (10) combined with winding topology analysis method (i.e. Fourier analysis of the MMF function) is introduced to solve the winding topology design problem. A typical design procedure is illustrated in gure 4.18, where two dierent types of design parameters can be considered, which are illustrated in gure 4.19. 

Geometric property of coils as design parameters Such method considers one phase winding as a series connection of coils where each coil is described by using three design parameters (gure 4.19a): the normalized coil pitch $\beta _ { c , n }$ , the normalized coil position $\alpha _ { c , n }$ and the normalized number of turns $N _ { c , n }$ . The optimization criteria are the maximization of the Winding factor of the working harmonic and the minimization of the THD of the winding factor harmonic spectrum. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/f7aca97799a866109007fe3f6fdd326f0ffbb0e61f46abf890a01f0cec1d9fa1.jpg)



Figure 4.18.: The design procedure by using stochastic approach


Three constraints are used to reduce the complexity of the problem: 

 The number of slots $N _ { s }$ is an even number which is a multiple of the number of phases m. 

 The max. number of winding layers $N _ { l }$ is limited to 2. 

 The winding topology is symmetrical and balanced which means each coil must have another coil diametrically opposite of the same number of turns and all the phase windings are with the same winding topology. 

Such approach is applied by N. Bekka [8, 7] for the special case of single tooth coil winding. A similar approach is also introduced by A.C. Smith et al. [65] where all the coils are assumed to have the same number of turns and the constraint of single tooth coil winding is removed (11). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/06ac527b79376055c05cba72e1628e107bfff060463596ea870143027ab95783.jpg)



(a) Geometric property of coils as design parameters


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/b9cfcafc623022c8b90657ee4fb90a22e25d8984961a46f51e6d70e32ccfca9d.jpg)



(b) MMF function as design parameters



Figure 4.19.: The Design Parameters of the stochastic approach


MMF function as design parameters In this approach, the MMF function of the multi-phase winding at a denite moment of time is considered as a series of rectangle-shaped function (gure 4.19b). Each rectangle function is characterized through two design parameters: position and amplitude, resulting in totally 2Ns independent design parameters [47]. 

A major drawback of such approach is that it is dicult to nd the corresponding winding topology for the optimized MMF function, which is an inverse problem and is more dicult to solve. Furthermore, it will be shown in the next chapter that the optimal MMF function for any given number of slots and pole pairs can be calculated in a deterministic way. 

# 4.3.2. Winding topology modication methods

In general, such methods are applied to over-harmonic winding topology, since the impacts of the sub-harmonic contents on the machine performance are quite strong (chapter 2). The purpose of the modication is to reduce the winding factor of the sub-harmonics. Dierent methods are introduced by various authors which can be classied into four groups. 

# 4.3.2.1. The multi-layer approach

Winding topology of multi-layer is understood as each slot is with more than two coil sides. The general modication procedure is quite simple and can be summarized as follows, which is illustrated in gure 4.20: 

1. Double the 2-layer winding. 

2. Shift the new winding set to a particular number of slots. 

3. Merge the two winding sets. 

Such approach is introduced by L. Alberti [2], M. V. Cistelecan [18, 17] and Q. Li [45] for modifying the over-harmonic winding topology with single tooth coil. 

# 4.3.2.2. The multi-slot approach

In the multi-slot approach, the modication is performed by increasing the increase of the number of slots. The general modication procedure is similar to the multi-layer approach and can be summarized as follows which is illustrated in gure 4.21: 

1. Double the slots and the double-layer winding. 

2. Shift the new winding set to a particular number of slots. 

3. Merge the two winding sets. 

Since the number of slots is doubled, the coil pitch (measured as number of slots) is also doubled. Such approach was rstly introduced by H. Kometani et al. [43] and further followed by G. Dajaku et al. [19] and R. B. Reddy [56, 57]. An Extension of the special case of 3-phase winding with 12 slots and 10 poles to a 6-phase winding is introduced by N. Domann [24]. 

# 4.3.2.3. The multi-turn approach

In the multi-turn approach, the modication is performed by changing the number of turns of the coils. In general, such approach is combined with the multi-layer approach and is served as a post-modication of the obtained multi-layer winding. The purpose of the post-modication is to reduce the number of layers and to improve the performance of the winding topology further. The discussion about the modication procedure on a particular winding topology can be found in [18, 17, 19, 42]. The general modication procedure can be summarized as follows which is illustrated in gure 4.22: 

1. For the coils of one phase winding, draw the star of coils for the considered sub-harmonic (not the working harmonic!) 

2. From the star of coils, choose the coils for the modication, 

3. Add the phasors of the coils and calculate the winding factor, 

4. Change the number of turns of the particular coil and see how the winding factor changes. 

The diculty of this approach lies on point 2, which is problem dependent and depends on the person who considers the problem. For the example given in gure 4.22, the fundamental harmonic is fully canceled if $a = \sqrt { 3 } b$ . 

# 4.3.2.4. The multi-conductor approach

In the multi-conductor approach, the modication is performed by using coils with a dierent number of conductors per coil side. It is possible to wound a coil in such a way that the one coil side has one more conductor as the other coil side as illustrated in gure 4.23. For this case, the two connections of the coil are on the both sides of the stator. 

By using such technique, the conductor ratio of the both coil sides can be varied from 0.5 (for case $a = 1 , b = 2 )$ to near 1 (for case $a = 1 0 0 , b =$ 101). Such approach is rstly introduced by G. Dajaku et al. [20] and further applied by C. Veeh in his doctoral thesis [78]. 

The general modication procedure is similar as that given in the previous approach. Instead of using the star of coils, the star of slots is used. The number of conductors per coil side is considered as modi- cation variables, instead of the number of turns per coil. Due to the constraint $b = a + 1$ , the number of modication variables remains the same. Such approach also faces the same diculty as mentioned in the previous approach. 

A major drawback of this approach is that the solution leads to a de- nite number of conductors, which makes the winding topology depending on the total number of conductors. In contrast, the solution of the previous approaches gives a denite ratio between the number of turns of the coils. This means that when this ratio is kept, the total number of turns of the winding topology be exibly changed, without changing the winding performance. The advantage of such approach is that the resulting winding topology is a double-layer winding which is quite simple to manufacture. 

# 4.3.2.5. The multi-coil approach

In the multi-coil approach, coils are modied so that they are with a dierent number of turns and coil pitch. This approach is rst introduced by H. Schack-Nielsen [61] in the year 1940 for the modication of the fundamental harmonic winding. Although dierent examples are given in the paper, a unied and systematical modication procedure is not given. 

A method based on an entirely dierent point of view also leads to such winding topology, which is proposed in [11] by the author for the overharmonic winding. According to the author's knowledge, it is the rst time to introduce such topology for the over-harmonic winding (gure 4.24). The major advantage of such topology is that the winding factor harmonic spectrum is very good and the structure of winding is quite simple. 

Unlike the winding modication methods, the method introduced by the author calculates the coil pitch as well as the number of turns by solving an over-determined system of linear equations. The mathematical basis, as well as the design procedures, are introduced in the next chapters. A detailed discussion of the example given in gure 4.24 can be found in chapter 6. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/0b74de3edfde99de748ce7902d67640d81083e01abab095866ec779eb953d10a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/38843d57323763cc8debc867717b178b7c21e384b579fda6f025e0d1f1f44cd1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/d4aecfefdef5c58618ad7b3bbe8fd0b9f475005dc33d0d6b186d8891c7bc2d30.jpg)



(a) The double-layer winding topology of phase A



(b) The second winding set with a rotation step of 5 slot pitch



(c) The 4-Layer winding topology of phase A


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/99384425b11c318097c0f28e4f3868bdc6532301a2bc679d26ee9bbb942d4eb6.jpg)



(d) Impact of the rotation steps on the winding factors



Figure 4. 20. : The multi-layer modication approach


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/4eeddc0fe47f0579b433a68925f79daa7bda8dceea2d607423e1ca934682c471.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/85db7e455f0c83b40a686aca6a5636f4999b76495c55468956ece7ca6cfec5e6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/171ad7a8c18c217e8ff0bb4664f7a02dc0a4f3847139ecd1dde94b4936f56742.jpg)



(a) The winding topology of phase A after doubling the number of slots



(b) The second winding set with a rot ation step of 1 slot pitch



(c) The double-Layer winding of phase A with double number of slots


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2221724f7aaff4f5c6e03cc71afd13b68ade98a2ae65ba9e3b007d9c391cbf6a.jpg)



(d) Impacts of rotation steps on the winding factors



Figure 4. 2 1 . : The multi-slot modication approach


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/363fc145d0fa871ffae0d5275895ae8c17a71c5e12607c4cf6b55fa88ea6573b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/0a7f508430d464ce8ca951b37944272356768f4bd335024767f70e0c2beff7f9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/9c841eb01fe0ef68ccc9df3c65642fcdf8ddad494f8cafc43eae55b9f560e98d.jpg)



(a) The winding topology of phase A



(b) The star of coils of the fundamental harmonic



(c) The star of coils of the 5-th harmonic


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/04c58c0b34553e38fd22fe92014264a2bec70017053e1179325e2681cdc6e167.jpg)



(d) Impacts of turn ratio on the winding factors



Figure 4. 22 . : The multi-turn modication approach


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/dbde3a67e63cc5dec406d1f44429ce5059a66ef775507fde86ef3b307e43404c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/bf5b951ec275d428f53a049a8edffac06376fdfa9199e61413a9b41776d3d2b2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/adba1a4ea0b3da42f64e892a777429aa1787b08d11803bba24f4b30d57c557e3.jpg)



(a) The winding topology of phase A



(b) The star of coils of the fundamental harmonic



(c) The star of coils of the 5-th harmonic


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/6b824f5e57e6e7d1fdc04d9ef2ae73995c0810df466052bed1bc91abb0543aba.jpg)



(d) Impacts of number of conductors on the winding factors



Figure 4. 23. : The multi-conductor modication approach


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a3d3c5313be2182846a10e38d5461bc4c4ca51ea3b5d4f99a3ecb50b3a24734d.jpg)



(a) The winding topology of phase A


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a5e7c1902c7f38a2a611e2ad338152a1cb90cb9fb3b2a863abcc8ffdd2292bd1.jpg)



(b) The winding factor harmonic spectrum



Figure 4.24.: The multi-coil approach


# 5. A unied method for the treatment of the winding topology

# 5.1. Assumptions

The winding topology considered is with $N _ { s }$ slots, fed with a m-phase current system and should a traveling wave with a space harmonics order of γ. 

The objective is to nd out how to construct the multi-phase winding with coils so that it gives the optimal winding factor harmonic spectrum under the considered design constraints. Since for a pure topological consideration, whether the coils are the parallel or serial connected is irrelevant. In this thesis, all the coils are assumed to be connected in series. 

Under this preamble, the discussion in the next sections is based on the following assumptions: 

 It is to assume that the greatest common divisor of $N _ { s }$ and $\gamma$ is 1: 

$$
\operatorname * {g c d} (N _ {s}, \gamma) = 1 \tag {5.1}
$$

This ensures that the winding topology discussed is elementary and it cannot be constructed from other elementary winding topologies. 

 Each phase current is a sinusoidal function in time with the same amplitude $\hat { i }$ and frequency $\omega$ but dierent current phase $\phi _ { k }$ : 

$$
i _ {k} (t) = \hat {i} \cdot \cos (\omega t + \phi_ {k}) \tag {5.2}
$$

 The slots are uniformly distributed along the stator circumference. Without losing the topological property of the winding, the circumference of the stator is chosen as 1. This leads to that the position 

of the n-th slot is (1): 

$$
x _ {n} = \frac {1}{N _ {s}} \cdot n \tag {5.3}
$$

 Within each slot, there are conductors of dierent number and winding direction, fed with currents of dierent phases. The total MMF of the n-th slot is then: 

$$
\Theta_ {n} (t) = \sum_ {k = 0} ^ {m - 1} \Theta_ {n, k} (t) = \sum_ {k = 0} ^ {m - 1} c _ {n, k} \cdot i _ {n, k} (t) \tag {5.4}
$$

where $c _ { n , k }$ can be chosen from negative integer, zero or positive integer: 

$$
c _ {n, k} \in \{\pm g, 0 \}, \quad g: \text { integer } \tag {5.5}
$$

The sign of $c _ { n , k }$ gives the information about the winding direction of the conductors while the absolute value gives the information about the number of conductors. 

 The MMF distribution of each slot is regarded as a spatial Dirac impulse which is distributed in the middle of the slot. The MMF distribution along the stator circumference is a superposition of each MMF, which is named as MMF space distribution, current sheet (in German Strombelag) or MMF space function in this thesis: 

$$
\Theta (x, t) = \sum_ {n = 0} ^ {N _ {s} - 1} \Theta_ {n} (t) \cdot \delta (x - x _ {n}) \tag {5.6}
$$

# 5.2. The theoretical and mathematical Basis

# 5.2.1. Derivation of the analytical formula for the calculation of winding factor of arbitrary space harmonic order

The Fourier analysis of the MMF spatial distribution provides the theoretical basis of the method. The MMF spatial distribution $\Theta ( x , t )$ can be seen as a superposition of the complex Fourier series: 

$$
\Theta (x, t) = \sum_ {\nu = - \infty} ^ {+ \infty} C _ {\nu} (t) \mathrm{e} ^ {j \nu 2 \pi x} \tag {5.7}
$$

where ν is the space harmonic order. 

The Fourier coecient $C _ { \nu }$ can be calculated as: 

$$
C _ {\nu} (t) = \int_ {0} ^ {1} \Theta (x, t) \mathrm{e} ^ {- j \nu 2 \pi x} \mathrm{d} x \tag {5.8}
$$

According to the assumptions in the previous section (equation 5.2, 5.4, 5.6), $\Theta ( x , t )$ can be formulated as: 

$$
\Theta (x, t) = \sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {k = 0} ^ {m - 1} \mathrm{Re} \left\{\hat {\Theta} _ {n, k} \mathrm{e} ^ {j (\omega t + \theta_ {k})} \right\} \delta (x - x _ {n}) \tag {5.9}
$$

where $\hat { \Theta } _ { n , k } = c _ { n , k } \cdot \hat { i } .$ 

On substituting 5.9 into 5.8, an equation to calculate the coecient $C _ { \nu } ( t )$ is obtained: 

$$
C _ {\nu} (t) = \sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {k = 0} ^ {m - 1} \mathrm{Re} \left\{\hat {\Theta} _ {n, k} \mathrm{e} ^ {j (\omega t + \theta_ {k})} \right\} \mathrm{e} ^ {- j \nu 2 \pi x _ {n}} \tag {5.10}
$$

where the property of the Dirac impulse function $\delta ( x - x _ { n } )$ is used: 

$$
f (x _ {n}) = \int_ {0} ^ {T} f (x) \cdot \delta (x - x _ {n}) \mathrm{d} x \tag {5.11}
$$

where T is the period of the function $f ( x )$ . 

On substituting 5.10 into 5.7, the MMF space distribution can be expressed as: 

$$
\Theta (x, t) = \sum_ {\nu = - \infty} ^ {+ \infty} \sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {k = 0} ^ {m - 1} \mathrm{Re} \left\{\hat {\Theta} _ {n, k} \mathrm{e} ^ {j (\omega t + \theta_ {k})} \right\} \mathrm{e} ^ {j \nu 2 \pi (x - x _ {n})} \tag {5.12}
$$

By using: 

$$
\operatorname{Re} \left\{\hat {\Theta} _ {n, k} \mathrm{e} ^ {j (\omega t + \theta_ {k})} \right\} = \frac {1}{2} \left(\hat {\Theta} _ {n, k} \mathrm{e} ^ {j (\omega t + \theta_ {k})} + \hat {\Theta} _ {n, k} \mathrm{e} ^ {- j (\omega t + \theta_ {k})}\right) \tag {5.13}
$$

Equation 5.12 changes to: 

$$
\begin{array}{l} \Theta (x, t) = \frac {1}{2} \sum_ {\nu = - \infty} ^ {+ \infty} \sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {i = 1} ^ {m - 1} \hat {\Theta} _ {n, k} \left[ \mathrm{e} ^ {j (\omega t + \nu 2 \pi x)} \cdot \mathrm{e} ^ {j (\phi_ {k} - \nu 2 \pi x _ {n})} \right. \tag {5.14} \\ \left. + \mathrm{e} ^ {- j (\omega t - \nu 2 \pi x)} \cdot \mathrm{e} ^ {- j (\phi_ {k} + \nu 2 \pi x _ {n})} \right] \\ \end{array}
$$

where the time and space dependent terms are combined into the terms $\mathrm { e } ^ { j ( \omega t + \nu 2 \pi x ) }$ and $\mathrm { e } ^ { - j ( \omega t - \nu 2 \pi x ) }$ , which are a one dimensional wave functions. 

Because addition is associative, equation 5.14 can be rewritten as: 

$$
\Theta (x, t) = \frac {1}{2} \sum_ {\nu = - \infty} ^ {+ \infty} \sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {k = 0} ^ {m - 1} \hat {\Theta} _ {n, k} \left[ \mathrm{e} ^ {j (\omega t + \nu 2 \pi x)} \cdot \mathrm{e} ^ {j \left(\phi_ {k} - \nu 2 \pi x _ {n}\right)} \right] \tag {5.15}
$$

$$
+ \frac {1}{2} \sum_ {\nu = - \infty} ^ {+ \infty} \sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {k = 0} ^ {m - 1} \hat {\Theta} _ {n, k} \left[ \mathrm{e} ^ {- j (\omega t - \nu 2 \pi x)} \cdot \mathrm{e} ^ {- j (\phi_ {k} + \nu 2 \pi x _ {n})} \right]
$$

Moreover, addition is commutative, the second term of equation 5.15 can be rewritten as: 

$$
\frac {1}{2} \sum_ {\nu = - \infty} ^ {+ \infty} \sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {k = 0} ^ {m - 1} \hat {\Theta} _ {n, k} \left[ \mathrm{e} ^ {- j (\omega t - \nu 2 \pi x)} \cdot \mathrm{e} ^ {- j \left(\phi_ {k} + \nu 2 \pi x _ {n}\right)} \right] \tag {5.16}
$$

$$
= \frac {1}{2} \sum_ {\nu = - \infty} ^ {+ \infty} \sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {k = 0} ^ {m - 1} \hat {\Theta} _ {n, k} \left[ \mathrm{e} ^ {- j (\omega t + \nu 2 \pi x)} \cdot \mathrm{e} ^ {- j (\phi_ {k} - \nu 2 \pi x _ {n})} \right]
$$

On substituting equation 5.16 into 5.15, the following formula for the description of the MMF space distribution of the winding is obtained: 

$$
\Theta (x, t) = \sum_ {\nu = - \infty} ^ {+ \infty} \operatorname{Re} \left\{\sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {k = 0} ^ {m - 1} \hat {\Theta} _ {n, k} \left[ \mathrm{e} ^ {j (\omega t + \nu 2 \pi x)} \cdot \mathrm{e} ^ {j (\phi_ {k} - \nu 2 \pi x _ {n})} \right] \right\} \tag {5.17}
$$

which is the real part of a complex wave function. 

To characterize the complex MMF wave , a complex phasor of arbitrary space harmonic order ν is introduced as: 

$$
\underline {{{{\Theta}}}} _ {\nu} = \sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {k = 0} ^ {m - 1} \hat {\Theta} _ {n, k} \mathrm{e} ^ {j (\phi_ {k} - \nu 2 \pi x _ {n})} \tag {5.18}
$$

By considering assumption 3 of the previous section, equation 5.18 becomes: 

$$
\underline {{\Theta}} _ {\nu} = \sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {k = 0} ^ {m - 1} \hat {\Theta} _ {n, k} \mathrm{e} ^ {j (\phi_ {k} - \nu \frac {2 \pi}{N _ {s}} n)} \tag {5.19}
$$

which indicates that the phasors of two complex MMF waves are identical, if the interval of the space harmonic orders is a multiple of the slot number $N _ { s }$ : 

$$
\underline {{\Theta}} _ {\nu} = \underline {{\Theta}} _ {k \cdot N _ {s} + \nu}, \quad k: \text { integer } \tag {5.20}
$$

Such eect is caused by the discrete distribution of the MMF function, and is referred as slot harmonic in the classical textbook [63]. This means, the MMF space harmonic spectrum is a periodical function with a period equal to the total number of slots $N _ { s }$ . Under this statement, it's necessary and sucient to consider the MMF space harmonic spectrum within one period, which is chosen as follows in this thesis(2): 

$$
\nu \in [ \nu_ {0}, \nu_ {N _ {s} - 1} ], \quad \nu_ {0}, \nu_ {N _ {s} - 1} = \left\{ \begin{array}{l l} - \frac {N _ {s}}{2}, \frac {N _ {s}}{2} - 1 & N _ {s}: \text { even   number } \\ - \frac {N _ {s} + 1}{2}, \frac {N _ {s} - 1}{2} & N _ {s}: \text { odd   number } \end{array} \right. \tag {5.21}
$$

Since the topological properties of a multi-phase winding are independent on the total number of conductors of the winding $\sum \sum \left| c _ { n , k } \right|$ and the amplitude of the phase current $\hat { i } .$ Two windings are topologically considered as the same, if: 

$$
c _ {n, k} ^ {\prime} = k \cdot c _ {n, k}, \quad k: \text { integer } \tag {5.22}
$$

$$
\hat {i} ^ {\prime} = r \cdot \hat {i}, \quad r \colon \mathrm{realnumber}
$$

although the complex phasors $\boldsymbol { \Theta } _ { \nu } ^ { \prime } \neq \boldsymbol { \Theta } _ { \nu }$ . 

Therefore, for a pure topological consideration, a phase current amplitude $\hat { i }$ and total number of conductors $\sum \sum | c _ { n , k } |$ independent factor should be introduced, which can be obtained by dividing the complex MMF phasor $\Theta _ { \nu }$ through $\hat { i } \cdot \sum \sum | c _ { n , k } |$ , leading to the denition of the 

winding factor $\xi _ { \nu }$ : 

$$
\begin{array}{l} \underline {{\xi}} _ {\nu} = \frac {\underline {{\Theta}} _ {\nu}}{\sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {k = 0} ^ {m - 1} | c _ {n , k} | \cdot \hat {i}} \\ = \frac {1}{\sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {k = 0} ^ {m - 1} \left| c _ {n , k} \right|} \sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {k = 0} ^ {m - 1} c _ {n, k} \mathrm{e} ^ {j \left(\phi_ {k} - \nu \frac {2 \pi}{N _ {s}} n\right)} \tag {5.23} \\ = \sum_ {n = 0} ^ {N _ {s} - 1} \left(\sum_ {k = 0} ^ {m - 1} \frac {1}{\sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {k = 0} ^ {m - 1} | c _ {n , k} |} \cdot c _ {n, k} \cdot \mathrm{e} ^ {j \phi_ {k}}\right) \mathrm{e} ^ {- j \nu \frac {2 \pi}{N _ {s}} n} \\ \end{array}
$$

The magnitude of $\boldsymbol { \xi } _ { \nu }$ is always equal or less than 1, since $\left| \mathrm { e } ^ { j x } \right| \le 1$ . Similar to the MMF harmonic spectrum, the winding factor harmonic spectrum has also a period of $N _ { s }$ . 

# 5.2.2. Calculation of the winding factor space harmonic spectrum using matrix notation

A compact and elegant way to calculate the winding factors for one period of the space harmonic order is to formulate equation 5.23 by using the matrix notation, which is shown as follows: 

 The symmetrical m-phase current system is considered as a $m \times 1$ vector $\underline { { \phi } } { : }$ : 

$$
\underline {{\phi}} = \left[ \begin{array}{c c c c} \mathrm{e} ^ {j \phi_ {0}} & \mathrm{e} ^ {j \phi_ {1}} & \dots & \mathrm{e} ^ {j \phi_ {m - 1}} \end{array} \right] ^ {\mathrm{T}} \tag {5.24}
$$

 The conductor distribution of the multi-phase winding is mathematically formulated as a matrix of $N _ { s }$ rows and m columns, where the rst index of the element $c _ { n , k }$ identies the slot position of the conductor and the second index identies the phase aliation. In this Thesis, such matrix is named as conductor distribution matrix C: 

$$
\mathbf {C} = \left[ \begin{array}{c c c c} c _ {0, 0} & c _ {0, 1} & \dots & c _ {0, m - 1} \\ c _ {1, 0} & c _ {1, 1} & \dots & c _ {1, m - 1} \\ \vdots & \vdots & \ddots & \vdots \\ c _ {N _ {s} - 1, 0} & c _ {N _ {s} - 1, 1} & \dots & c _ {N _ {s} - 1, m - 1} \end{array} \right] \tag {5.25}
$$

 The total MMF distribution is then the product of the conductor distribution matrix C and the m-phase current system $\underline { { \phi } } \mathrm { : }$ 

$$
\underline {{{{\Theta}}}} = \mathbf {C} \cdot \underline {{{{\phi}}}} \tag {5.26}
$$

which is a $N _ { s } \times 1$ vector. 

 The transformation from the MMF distribution to the MMF space harmonic spectrum within the period $\boldsymbol \nu \in \left[ \boldsymbol \nu _ { 0 } , \boldsymbol \nu _ { N _ { s } - 1 } \right]$ is considered as a square matrix $\mathbf { M } _ { \nu }$ with complex elements: 

$$
\underline {{\mathbf {M}}} _ {\nu} = \left[ \begin{array}{c c c c} \mathrm{e} ^ {- j \nu_ {0} \frac {2 \pi}{N _ {s}} 0} & \mathrm{e} ^ {- j \nu_ {0} \frac {2 \pi}{N _ {s}} 1} & \dots & \mathrm{e} ^ {- j \nu_ {0} \frac {2 \pi}{N _ {s}} (N _ {s} - 1)} \\ \mathrm{e} ^ {- j \nu_ {1} \frac {2 \pi}{N _ {s}} 0} & \mathrm{e} ^ {- j \nu_ {1} \frac {2 \pi}{N _ {s}} 1} & \dots & \mathrm{e} ^ {- j \nu_ {1} \frac {2 \pi}{N _ {s}} (N _ {s} - 1)} \\ \vdots & \vdots & \ddots & \vdots \\ \mathrm{e} ^ {- j \nu_ {N _ {s} - 1} \frac {2 \pi}{N _ {s}} 0} & \mathrm{e} ^ {- j \nu_ {N _ {s} - 1} \frac {2 \pi}{N _ {s}} 1} & \dots & \mathrm{e} ^ {- j \nu_ {N _ {s} - 1} \frac {2 \pi}{N _ {s}} (N _ {s} - 1)} \end{array} \right] \tag {5.27}
$$

so that: 

$$
\underline {{\boldsymbol {\Theta}}} _ {\nu} = \underline {{\mathbf {M}}} _ {\nu} \cdot \underline {{\boldsymbol {\Theta}}} \tag {5.28}
$$

 As mentioned before, in order to purely characterize the topology properties, the number of conductors per slot $c _ { n , k }$ should be normalized by the total number of conductors $\sum \sum | c _ { n , k } |$ . This leads to the denition of the normalized conductor distribution matrix C, which is: 

$$
\overline {{\mathbf {C}}} = \frac {1}{\sum_ {n = 0} ^ {N _ {s} - 1} \sum_ {k = 0} ^ {m - 1} \left| c _ {n , k} \right|} \cdot \mathbf {C} \tag {5.29}
$$

Since the winding topology is fully characterized by the normalized conductor distribution matrix, such matrix is also named as winding topology matrix in this thesis. 

 A normalized MMF distribution is then dened as: 

$$
\overline {{\boldsymbol {\Theta}}} = \overline {{\mathbf {C}}} \cdot \underline {{\phi}} \tag {5.30}
$$

 The winding factor space harmonic spectrum is then: 

$$
\underline {{\boldsymbol {\xi}}} _ {\nu} = \underline {{\mathbf {M}}} _ {\nu} \cdot \overline {{\boldsymbol {\Theta}}} = \underline {{\mathbf {M}}} _ {\nu} \cdot \overline {{\mathbf {C}}} \cdot \underline {{\boldsymbol {\phi}}} \tag {5.31}
$$

# 5.2.3. The unique mapping of the winding factor harmonic spectrum and the normalized MMF distribution

It can be shown that, the square transformation matrix $\mathbf { M } _ { \nu }$ is always invertible with: 

$$
\underline {{\mathbf {M}}} _ {\nu} ^ {- 1} = \mathbf {H} \cdot \underline {{\mathbf {M}}} _ {\nu} ^ {\mathrm{T}} \tag {5.32}
$$

where the element of the $N _ { s } \times N _ { s }$ matrix H is (3): 

$$
H _ {n, k} = \left\{ \begin{array}{l l} 0, & n + k \neq N _ {s} - 2 \\ \frac {1}{N _ {s}}, & n + k = N _ {s} - 2 \end{array} \right. \tag {5.33}
$$

It means that for each winding factor harmonic spectrum $\underline { { \xi } } _ { \nu } .$ , there is always a corresponding normalized MMF distribution $\overline { { \Theta } } ,$ , which is: 

$$
\overline {{{\boldsymbol {\Theta}}}} = \mathbf {H} \cdot \underline {{{\mathbf {M}}}} _ {\nu} ^ {\mathrm{T}} \cdot \underline {{{\boldsymbol {\xi}}}} _ {\nu} \tag {5.34}
$$

Therefore, it is not necessary to use a stochastic algorithm (e.g. Generic Algorithm) to nd out the corresponding normalized MMF distribution for a desired winding factor harmonic spectrum, as done in [47]. 

# 5.2.4. The graphical presentation of the matrix notation

In general, the winding topology treatment method is known that it is quite abstract, dealing with numbers. Therefore, it is very important to introduce a graphical representation of the method, so that it can be better understood and widely spread. Moreover, such graphical representation can also be used as a graphical design tool. 

Based on this consideration, a great eort has been done during this thesis for the illustration of the proposed method. The graphical representation is based on the illustrations of the matrices introduced in the previous section: $\underline { { \boldsymbol { \xi } } } _ { \nu } , \overline { { \Theta } } , \overline { { \mathbf { C } } } , \underline { { \boldsymbol { \phi } } }$ . They which will be discussed in the following sections. 

Illustrations of the fundamental and over-harmonic winding topology of 3 phases and 12 slots (gure 4.2) are used as examples. 

# 5.2.4.1. The winding factor harmonic spectrum

Since the winding factor space harmonic is periodic, a new representation form is introduced in this thesis, which illustrates the winding factor harmonic spectrum not in the classical Cartesian coordinate system (gure 5.1a) but the polar coordinate system with $N _ { s }$ increments (gure 5.1b). 

The winding factor of each harmonic order in 5.1b is illustrated as a complex phasor with the length representing the winding factor and the phase representing the harmonic order. The harmonic order starts with zero, along with the clockwise direction, the harmonic order decreases by one after each increment and along the anticlockwise direction, the harmonic order increases by one after each increment. 

This novel representation form has the advantage that the periodicity of the winding factor harmonic spectrum is automatically included by the property of the polar coordinate system. When compared with the classical representation form, such illustration is more compact and clear without redundant information. 

# 5.2.4.2. The normalized MMF distribution

Since each element of the normalized MMF distribution is a complex number, which can also be interpreted as a phasor. It is more suitable to illustrate it in the polar coordinate system. Beside the amplitude and phase, the position of each MMF phasor needs to be underlined. To emphasize that, each MMF phasor is assigned with a real number indicating its position. 

The normalized MMF distribution of the investigated fundamental and over-harmonic winding topology given in gure 4.2 are illustrated in gure 5.2. Dierent lengths of the normalized MMF phasors are observed. This leads to the appearance of the sub- and over-harmonic contents in the winding factor harmonic spectrum given in gure 5.1. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/947995b9bc05a768bbe3b77ed7f6d6b87e2a12287b5f15d78f60535492d6585d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e50a994b349c6a9d6cac261ed807cb63b68c36d3f3db88bce7776c97283e6777.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2803b311fe3fd93b817983fb656f09f6b975e7efa9f78f013581b7c72b9adfb0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/6b241affb807883c1876551a207f82f7d5b96d18ab8868c2c2bc29d72ae15f80.jpg)



(a) The classical presentation form, up: working harmonic $\gamma = 1$ , bottom: working harmonic $\gamma = - 5$



(b) The novel presentation form, up: working harmonic $\gamma = 1$ , bottom: working harmonic $\gamma = - 5$



Figure 5.1.: A novel representation form of the winding factor harmonic spectrum with the periodicity of the winding factor harmonic spectrum automatically included by the periodicity of the polar coordinate system


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/fdf9b0462af0a293356510278472bfee86cd5d9243131ff0af54f3c9fa018c51.jpg)



(a) The normalized MMF distribution of the fundamental harmonic winding with $\gamma = 1$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2caf71b0008fbe84487d662bf5a493d47dbcec004ba5bd1aebf52cc5dd879fec.jpg)



(b) The normalized MMF distribution of the over-harmonic winding with γ = −5



Figure 5.2.: Illustration of the normalized MMF distribution with 12 slots. Each MMF phasor has an index, indicating its slot position.


# 5.2.4.3. The symmetrical multi-phase current system

As mentioned in the previous section, the symmetrical multi-phase current system is considered as a vector with m elements of complex number $\phi .$ . It can be illustrated as m phasors with dierent angle $\phi _ { k }$ and a unity amplitude in the polar coordinate system. 

Two examples are given in gure 5.3a and 5.3b for $m = 3$ and $m = 6$ . The 6-phase current system is combined from two 3-phase current system shifted by an angle of 30 degree. It seems that the symmetrical property of the 6-phase current system is not better than that of the 3-phase current system, because for both cases, a rotational symmetry of order 3 (4) is observed. It is not the case if the winding direction is considered. This is discussed in the next subsection. 

# 5.2.4.4. The winding direction

MMF of conductors with negative winding direction can be interpreted in two dierent ways: 

$$
\underline {{\Theta}} _ {n, k} = (- 1 \cdot | c _ {n, k} |) \cdot \underline {{\phi}} _ {k} = | c _ {n, k} | \cdot \left(- 1 \cdot \underline {{\phi}} _ {k}\right) \tag {5.35}
$$

It will be shown later that for a better illustration of the conductor distribution matrix C as well as the winding topology C, it is better to use the second way to represent the winding direction. This means to extend the symmetrical m-phase current system to m more phasors with φk+m $\underline { { \phi } } _ { k + m } = - \underline { { \phi } } _ { k }$ . This results in 2m around 2π symmetrically distributed phasors with phase of adjacent phasors $\pi \div m$ , independent on if the number of phases m is an odd or even number (gure 5.3c and 5.3d). 

By using the symmetrical multi-phase current system with winding direction considered, an elegant and beautiful presentation form for the winding topology C can be achieved. This is discussed in the next subsection. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/767900d8960cb7a7154be4952955688a60515670dd7aa32996b7df796cc48a11.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/652d4c1ca9488278e31b983361aa4cb7dec0497da50065d5c02f2f9788896b7b.jpg)



(a) The 3-phase symmetrical current system



(b) The 6-phase symmetrical current system


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/5a18402aead57df2ffd6303f956b9d0a69d729dbcaf630420a2f6e1ec8f986e8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/c610e9c2605f9f6ea9e3015fda8f9487d75b1e305ddb291e37bc8779e31ab48f.jpg)



(c) The 3-phase symmetrical current system with winding direction considered



(d) The 6-phase symmetrical current system with winding direction considered



Figure 5.3.: Illustration of the symmetrical multi-phase current system


# 5.2.4.5. The normalized conductor distribution matrix: topology of the multi-phase winding

Mathematically, the winding topology C transform the symmetrical multiphase current system $\underline { { \phi } }$ into the normalized MMF distributed Θ. As each element of $\overline { { \Theta } }$ and $\underline { { \phi } }$ can be illustrated by a phasor, the winding topology C gives the information how each phasor $\overline { { \Theta } } _ { n }$ is constructed by the phasors within ${ \underline { { \phi } } } .$ . 

This is illustrated in gure 5.4a for the investigated fundamental and over-harmonic winding topology. The normalized conductor distribution matrix of the both winding topologies are given as following: 

$$
\mathbf {C} _ {1} = \left[ \begin{array}{c c c c c c c c c c c c} + 1 & 0 & 0 & 0 & - 1 & - 2 & - 1 & 0 & 0 & 0 & + 1 & + 2 \\ 0 & 0 & + 1 & + 2 & + 1 & 0 & 0 & 0 & - 1 & - 2 & - 1 & 0 \\ - 1 & - 2 & - 1 & 0 & 0 & 0 & + 1 & + 2 & + 1 & 0 & 0 & 0 \end{array} \right] ^ {\mathrm{T}}
$$

$$
\mathbf {C} _ {5} = \left[ \begin{array}{c c c c c c c c c c c c} + 1 & 0 & 0 & 0 & - 1 & + 2 & - 1 & 0 & 0 & 0 & + 1 & - 2 \\ 0 & 0 & + 1 & - 2 & + 1 & 0 & 0 & 0 & - 1 & + 2 & - 1 & 0 \\ - 1 & + 2 & - 1 & 0 & 0 & 0 & + 1 & - 2 & + 1 & 0 & 0 & 0 \end{array} \right] ^ {\mathrm{T}}
$$

The red phasors in 5.4a are the normalized MMF distribution given in gure 5.2. The phase of each blue phasor is dened by the symmetrical multi-phase current system with winding direction considered given in 5.3. The length of each blue phasor gives the information that how many conductors belong to the particular phase in the particular slot position. The slot position is indicated by each red phasor. 

A more familiar way to show the normalized conductor distribution matrix is given in gure 5.4b. The colors indicate the phase aliation of the conductors, the symbols of $\circledcirc$ and $\otimes$ indicate the winding direction of the conductors, the numbers near the conductors indicate the number of conductors, and the numbers outside the stator contour indicate the slot position. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/b935f80216eb5a6d714a3d5219c988e7aa8273ccb89b81d67409aca779573c29.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/16cebb0f624785e5645dc2ea2168f7892c108eaf0f0e8868f5947a819a1ded39.jpg)



(a) As phasors in polar coordinate system


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/f8f4225f5d80fc705950cf76d76d0c0001ca4b20e78eb7cdf505a8aed31a6fe8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a8e5db954e40cd94515f76bea6bce949d33c0af714928c14f2ff09f293cdd7cf.jpg)



(b) As conductors in stator slots



Figure 5.4.: Illustration of the normalized conductor distribution matrix of the fundamental and the over-harmonic winding with 12 slots and 3 phases


# 5.3. A unied method for winding topology analysis

# 5.3.1. The analysis procedures

The purpose of this section is to introduce a unied method for winding topology analysis. The method is deduced from the mathematical consideration of the previous section. Such method is valid for winding topologies with an arbitrary number of phases and an arbitrary number of conductors in each slot. 

As it is mentioned before, the winding topology analysis is a direct problem. This is because, from the winding scheme, the winding factor space harmonic spectrum transformation matrix $\mathbf { M } _ { \nu }$ , the normalized conductor distribution matrix C and the phase current vector $\phi$ can be obtained. By directly using equation 5.31 the winding factor harmonic spectrum can be obtained. 

The analysis procedures are given as follows: 

1. Obtain the symmetrical multi-phase current system $\underline { { \phi } }$ . 

2. Obtain the conductor distribution matrix C from the winding schema. 

3. Calculate the winding topology $\overline { { \mathbf { C } } }$ by using equation 5.29. 

4. Calculate the normalized MMF distribution $\underline { { \overline { { \mathbf { e } } } } }$ using equation 5.30. 

5. Write down the transformation matrix $\mathbf { M } _ { \nu }$ using 5.27. 

6. Calculate the winding factor harmonic spectrum $\underline { { \boldsymbol { \xi } } } _ { \nu }$ within the period $\boldsymbol \nu \in [ \nu _ { 0 } , \nu _ { N - 1 } ]$ using equation 5.31, where the period is calculated using equation 5.21. 

7. Calculate the winding factor of arbitrary harmonic order $\xi _ { \nu }$ : 

$$
\xi_ {\nu} = \xi_ {k}, \quad k = \mathrm{mod} (\nu - \nu_ {0}, N _ {s}) + \nu_ {0}
$$

# 5.3.2. Implementation of the method in Python

The matrix notation enables a very simple implementation of the method by high-level languages (e.g. C, MATLAB, Python, etc.). As an example, the python source code for the winding topology analysis above is given in A.1 with only 13 lines (except comments). Applying the method to the investigated winding topologies given in gure 4.2 gives the same results shown in gure 5.1. 

# 5.4. A unied method for winding topology design

In this section, a unied winding topology design method is introduced which is a deterministic approach and is valid for an arbitrary number of slots and phases. Using the proposed method, winding topologies of different complexity levels can be obtained which are the optimal solutions under the considered design constraints. 

Since the winding topology design is an inverse problem, the design procedures are more complicated than the analysis procedure introduced in the previous section. However, the mathematical basis remains the same. 

By considering equation 5.31, the winding topology design problem is formulated to nd the normalized conductor distribution matrix $\overline { { \mathbf { C } } }$ where the winding factor harmonic spectrum $\underline { { \boldsymbol { \xi } } } _ { \nu } ,$ , the transformation matrix $\mathbf { M } _ { \nu }$ and the multi-phase current system $\underline { { \phi } }$ are given. Unfortunately, the solution can not be obtained by solving equation 5.31, since the unknown is a matrix (not a vector), and there are more unknowns $( N _ { s } \times m )$ ) than the number of equations $N _ { s }$ . To overcome this problem, a systematic design procedure is needed, which is introduced step by step in this section. 

In this section, the theoretical consideration under each design step is discussed and highlighted. The application of the method for design of fundamental and over-harmonic winding topology of dierent complexity levels is given in the next chapter in detail. 

# 5.4.1. The ideal winding factor harmonic spectrum

The design purpose is explained in short before discussing the design procedures. 

From the examples given in chapter 2, it is clear that the MMF harmonics not equal to the working harmonic increase saturation of the magnetic material, lead to additional electromagnetic losses and cause vibration of the machine. Therefore, the purpose of each winding topology design is to reach the optimal winding factor harmonic spectrum, which can be formulated as: 

$$
\xi_ {\nu} = \left\{ \begin{array}{l l} 1, & \quad \nu = \gamma \\ 0, & \quad \nu \neq \gamma \end{array} , \quad \nu \in [ - \infty , + \infty ] \right. \tag {5.36}
$$

From the discussion in section 5.2, due to the appearance of the slot harmonics, this goal can not be reached, since it requires an innite number of slots $N _ { s }  \infty$ . However, for a given nite number of slots $N _ { s }$ , within one harmonic spectrum period of $N _ { s }$ harmonic orders, it is possible to reach this goal. Thus a realistic goal of the winding topology design can be mathematically formulated as follows: 

$$
\xi_ {\nu} ^ {\prime} = \left\{ \begin{array}{l l} 1, & \quad \nu = \gamma \\ 0, & \quad \nu \neq \gamma \end{array} , \quad \nu \in [ \nu_ {0}, \nu_ {N _ {s} - 1} ] \right. \tag {5.37}
$$

As an example, the winding factor harmonic spectrum of the investigated 3-phase double layer over-harmonic winding of 12-slots (gure 4.2b) is given in gure 5.5a and the corresponding ideal winding factor harmonic spectrum is given in gure 5.5b. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/ce88aa90474cbc459f9496d6ff489d38e4be27a9ab66af963fab088ceb60313e.jpg)



(a) Real winding factor spectrum


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/046a9b63143abebc49a88082e0b348f47925f0d54e50d62209815ad01ed853fb.jpg)



harmonic (b) Ideal winding spectrum


factor harmonic 

Figure 5.5.: The real and ideal winding factor harmonic spectrum with $\gamma = - 5$ 

# 5.4.2. The ideal normalized MMF distribution

From equation 5.34, if the ideal winding factor harmonic spectrum is dened, the corresponding ideal normalized MMF distribution can be 

calculated as: 

$$
\overline {{{\boldsymbol {\Theta}}}} ^ {\prime} = \mathbf {H} \cdot \underline {{{\mathbf {M}}}} _ {\nu} ^ {\mathrm{T}} \cdot \underline {{{\boldsymbol {\xi}}}} ^ {\prime} \tag {5.38}
$$

where it can be shown that the normalized MMF in the n-th slot is: 

$$
\overline {{\Theta}} _ {n} ^ {\prime} = \frac {1}{N _ {s}} \cdot \mathrm{e} ^ {j \gamma \frac {2 \pi}{N _ {s}} n} \tag {5.39}
$$

A comparison of the normalized MMF distributions of the real and ideal winding factor harmonic spectrum given in gure 5.5 is given in gure 5.6. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/d5a47a6a4938323a29d4802d7875c328ff6812e0ad5348460d8884115a979186.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/5b26c386e63d3172b25cc965f3674ed89571eee422d13d6d62f0982355d2d6c9.jpg)



(a) Real normalized MMF distribution (b) Ideal normalized MMF distribution



Figure 5.6.: The real and ideal normalized MMF distribution with working harmonic $\gamma = - 5$


# 5.4.3. The symmetrical multi-phase current system

The complexity of the winding topology strongly depends on the relationship between the available number of phases m and the number of slots $N _ { s }$ , which falls into following three categories. 

# 5.4.3.1. Number of phases equal number of slots

If a $N _ { s } .$ -phase current system is available, the ideal normalized MMF can be realized with a Ns-phase single layer winding with each slot of 1N $N _ { s } .$ $\frac { 1 } { N _ { s } }$ normalized conductors, fed with current of phase $\begin{array} { r } { \phi _ { n } = \gamma \frac { 2 \pi } { N _ { s } } n } \end{array}$ N (5). This winding topology is named ideal $N _ { s } – \mathrm { p h a s e }$ single layer winding in this thesis, since it can generate an ideal winding factor harmonic spectrum. 

By considering the following relationship: 

$$
\overline {{\boldsymbol {\Theta}}} ^ {\prime} = \overline {{\mathbf {C}}} ^ {\prime} \cdot \underline {{\boldsymbol {\phi}}} ^ {\prime}
$$

The winding topology $\overline { { \mathbf { C } } } ^ { \prime }$ changes to a squares $N _ { s } \times N _ { s }$ matrix with the element of: 

$$
\overline {{c}} _ {n, k} ^ {\prime} = \left\{ \begin{array}{l l} \frac {1}{N _ {s}} & n = \mathrm{mod} (k \gamma , N _ {s}) \\ 0 & \mathrm{else} \end{array} \right.
$$

which is always positive. 

This means all the conductors have the same winding direction. Winding topologies with all conductors in one direction can be realized with coils of tubular form, which can be found in machines of tubular form [80] or rotational/linear machines with Gramme-Winding [14]. Another possibility is to use massive conductors with one side connecting to the current source and the other side connecting to a short circuit ring [21]. 

# 5.4.3.2. Number of phases equal half number of slots

This type of winding topology is possible only if $N _ { s }$ is an even number. When compared to the previous case, in order to obtain the ideal winding factor harmonic spectrum, the number of phases m can be reduced to half, if the conductors are wound in both directions: 

$$
\vec {c} _ {n, k} ^ {\prime \prime} = \left\{ \begin{array}{l l} + \frac {1}{N _ {s}} & \quad \text {if:} n = \mathrm{mod} (k \gamma , N _ {s}) <   \frac {N _ {s}}{2} \\ - \frac {1}{N _ {s}} & \quad \text {if:} n = \mathrm{mod} (k \gamma , N _ {s}) \geq \frac {N _ {s}}{2} \\ 0 & \quad \text {else} \end{array} \right.
$$

# 5.4.3.3. The other cases

From the previous discussions, it is clear that it makes no sense to have the number of phases more than the number of slots: $m > N$ (for N is odd) or half the number of slots $\begin{array} { r } { m > \frac { N } { 2 } } \end{array}$ (for N is even). As the cases of equal the number of slots or half the number of slots are discussed above, the further discussion is constrained to the cases: 

$$
m <   \left\{ \begin{array}{l l} N _ {s}, & N _ {s} \text {is odd} \\ \frac {N _ {s}}{2}, & N _ {s} \text {is even} \end{array} \right.
$$

The phases of the current system are chosen so that, together with their counterparts of negative winding direction, the angle between adjacent phases is: 

$$
\Delta \phi = \frac {\pi}{m} (5. 4 0)
$$

as illustrated in gure 5.3 

# 5.4.4. Topology of the normalized conductor distribution matrix: types of winding topology

If the normalized MMF distribution, as well as the symmetrical multiphase current system, are known, it is quite easy to obtain the normalized conductor distribution matrix through solving a system of linear equations. However, a deepening analysis shows that there is also a topology dierence between the conductor distribution matrices. This topology dierence will be discussed here in detail. In this thesis, the topology of the normalized conductor distribution matrix is named type of winding topology. 

The type of winding topology depends on the angle oset between the normalized MMF distribution and the symmetrical multi-phase current system, which is dened as $\Delta \alpha$ . 

It should be noted that the two winding topologies given in gure 5.4 for dierent working harmonics belong to the same type of winding topology since the topologies of the two conductor distribution matrices (the blue phasors) are the same. By ignoring the position index of the normalized MMF distribution, these two winding topologies given in 5.4a are equal to the winding topology given in gure 5.7a with $\Delta \alpha = 0$ , . This type of winding topology is named winding topology of type I in this thesis. 

A dierent type of winding topology for the same number of slots and phases is given in 5.7b with $\Delta \alpha \neq 0$ . It is considered as winding topology of type II. When compared to the winding topology of type I, in each slot of the winding topology of type II, there are always conductors of 2 dierent phases. 

From gure 5.7, it is clear that when $\Delta \alpha$ continuously changes from 0 to $2 \pi$ , the type of the winding topology changes periodically between type I and type II, due to the symmetrical property of the normalized MMF distribution and the multi-phase current system. 

To obtain the both types of winding topology, $\Delta \alpha$ is chosen as follows during the design process: 

$$
\Delta \alpha \left\{ \begin{array}{l l} = 0 & \text { for:   Type   I } \\ \neq 0 & \text { for:   Type   II } \end{array} \right. \tag {5.41}
$$

For winding type of II, $\Delta \alpha$ is chosen so that the obtained winding topology has the best symmetrical property. For the example given in 5.7, $\Delta \alpha$ is chosen to be $\frac { \pi } { N _ { s } }$ , so that the resulting winding topology has the sbest symmetrical property. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/c6024a6511d106b1562cc04b86955205520f9898916f8222d713755809a2dd27.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/084724951a8fe6db3cc786eedb2528fe17da84e48d7930aa192811358419b098.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/089b51f22e0cf174bedc36a14a4580ca4175d76da2ca06aaa1d770588afc5136.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/db5d7940cbbf779030fcb8194db8c3e1ced7e972e9998ebb6b194b167797ef47.jpg)



(a) Winding topology of type I with (b) Winding topology of type II with $\Delta \alpha = 0$ ∆α = πN $\begin{array} { r } { \Delta \alpha = \frac { \pi } { N _ { s } } } \end{array}$



Figure 5.7.: Types of winding topology for winding of 12 slots and 3 phases


# 5.4.5. Determination of the normalized conductor distribution matrix: the primitive double-layer multi-phase winding

To determine the normalized conductor distribution matrix, equation 5.26 is used. Each element of the matrix is calculated from: 

$$
\overline {{{{\Theta}}}} _ {n} = \sum_ {k = 0} ^ {m - 1} \bar {c} _ {n, k} \cdot \underline {{{{\phi}}}} _ {k} \tag {5.42}
$$

where $\overline { { \Theta } } _ { n }$ is considered as known (calculated from equation 5.39) and $\overline { { c } } _ { n , k }$ is considered as unknown. 

Under this consideration, the equation above is formulated in matrix form: 

$$
\underline {{\phi}} \cdot \overline {{c}} _ {n} = \overline {{\Theta}} _ {n} \tag {5.43}
$$

which is a system of one complex linear equation with m real unknowns. Thus the system is under-determined. To obtain a unique solution, additional constraints should be applied. 

From gure 5.7, it is clear that to uniquely represent each MMF phasor, it is necessary and sucient to use two current phasors. If the two current phasors are chosen in a way that the projection of the considered MMF phasor on them is the largest among the all possible projections, the algebraic length of the two current phasors will be the smallest. This gives an indication that less conductors will be used and the winding factor will become larger. Mathematically, this can be formulated as: 

$$
k _ {0}, k _ {1} = \operatorname{argmax} \left(\operatorname{proj} \left(\overline {{\Theta}} _ {n}, \underline {{\phi}}\right), 2\right) \tag {5.44}
$$

where the function proj $( \underline { { b } } , \underline { { a } } )$ gives the projection of the phasor $\underline b$ on each phasor $\underline { { a } } _ { k }$ and argmax $( \pmb { a } , n )$ returns the indices of the rst n largest values of the vector a. 

Under this consideration, equation 5.43 is reduced to: 

$$
\left[ \begin{array}{c c} \underline {{\phi}} _ {k _ {0}} & \underline {{\phi}} _ {k _ {1}} \end{array} \right] \cdot \left[ \begin{array}{l} \overline {{c}} _ {n, k _ {0}} \\ \overline {{c}} _ {n, k _ {1}} \end{array} \right] = \overline {{\Theta}} _ {n} \tag {5.45}
$$

with one complex linear equation with two real unknowns. This can be uniquely solved by separating the complex linear equation into two real linear equations for the real and imaginary parts: 

$$
\left[ \begin{array}{c} \overline {{c}} _ {n, k _ {0}} \\ \overline {{c}} _ {n, k _ {1}} \end{array} \right] = \left[ \begin{array}{c c} \operatorname{Re} \underline {{\phi}} _ {k _ {0}} & \operatorname{Re} \underline {{\phi}} _ {k _ {1}} \\ \operatorname{Im} \underline {{\phi}} _ {k _ {0}} & \operatorname{Im} \underline {{\phi}} _ {k _ {1}} \end{array} \right] ^ {- 1} \cdot \left[ \begin{array}{c} \operatorname{Re} \overline {{\Theta}} _ {n} \\ \operatorname{Im} \overline {{\Theta}} _ {n} \end{array} \right] \tag {5.46}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/290ad9ae92a48b53d056b98883b6e00e7977f5fc233e8d7cf4a69d3076ade9d0.jpg)



(a) The MMF phasor lies on phase A, corresponding to winding topology given in 5.7a


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/cf4770c7aea41e6542784b2f27871967683384436c4962ff4f68e8f53c542ffb.jpg)



(b) The MMF phasor lies between phase A and C, corresponding to winding topology given in 5.7b



Figure 5.8.: Illustration of the projection of one MMF phasor (the ideal MMF phasor in the rst slot, assigned with index 0) on the symmetrical multi-phase current system


A major advantage of such approach is that it is valid for any con- guration between $\overline { { \Theta } } _ { n } , \underline { { \phi } } _ { k _ { 0 } }$ , and $\underline { { \phi } } _ { k 1 }$ . This is illustrated in gure 5.8 for two typical congurations, where the corresponding system of equations is derived as follows: 

Figure 5.8a: $\left[ \overline { { c } } _ { 0 , 0 } \right] = \left[ \mathrm { e } ^ { j 0 ^ { \circ } } \right] ^ { - 1 } \cdot \mathrm { e } ^ { j 0 ^ { \circ } } \Rightarrow \left[ \overline { { c } } _ { 0 , 2 } \right] = \left[ 1 \right]$ ej120◦  j 0 ◦  − 1 ej0◦ (5.47) 

Figure 5.8b: $\left[ { \overline { { c } } } _ { 0 , 0 } \right] = \left[ \mathrm { e } ^ { j 1 5 ^ { \circ } } \right] ^ { - 1 } \cdot \mathrm { e } ^ { j 0 ^ { \circ } } \Rightarrow \left[ { \overline { { c } } } _ { 0 , 0 } \right] = \left[ { \begin{array} {{ c } { 0 . 8 1 6 5 } } \\ { - 0 . 2 9 8 9 } \end{array} } \right]$ c0,0 ej135◦ j15◦ −1 ej0◦ 

By applying the same procedures for all the MMF phasor, the normalized conductor distribution matrix C is obtained. In this thesis, the winding topology corresponded to the normalized conductor distribution matrix is termed as primitive double-layer multi-phase winding. 

# 5.4.6. Exploitation of the symmetrical properties of the primitive multi-phase winding

From the normalized conductor distribution matrix C which is shown in gure 5.9, it is clear that there are some types of symmetry in the normalized conductor distribution matrix C. 

From the topological point of view, the winding topology is a twodimensional geometry with the center xed in origin. Thus two types of symmetry are considerable for the normalized conductor distribution matrix C: the rotational symmetry and the mirror symmetry. 

From gure 5.9, it is clear that there is rotational symmetry between the phase windings and there is mirror symmetry within each phase winding. These two types of symmetry will be discussed in the next two subsections in detail. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/93eed829dac78116889511e9557e97a47eb7e527f48ff73891645796eb52e3cb.jpg)



(a) Normalized Conductor Distribution (b) Normalized Conductor Distribution matrix C of type I matrix C of type II


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/f73ae8c82e1dc11d593157a08b4505531a4d97f43705f487ca79dbb30d66f90c.jpg)



Figure 5.9.: Illustration of the normalized conductor distribution matrix C to underline its symmetrical properties


# 5.4.6.1. Rotational symmetry: the symmetry between the primitive phase windings

For a better explanation of the rotational symmetry, instead of formulating the normalized MMF distribution in matrix multiplication form (equation 5.30), the normalized MMF distribution is formulated in vector addition form as follows: 

$$
\overline {{\boldsymbol {\Theta}}} = \sum_ {k = 0} ^ {m - 1} \underline {{\phi}} _ {k} \cdot \overline {{\boldsymbol {c}}} _ {k} \tag {5.48}
$$

where $\overline { { c } } _ { k }$ is the $N _ { s } \times 1$ column vector of the normalized conductor distribution matrix, which is termed as normalized conductor distribution vector in this thesis. 

This vector formulation can be physically interpreted as to consider the total MMF distribution as a superposition of MMF distributions of particular phases. In contrast, the matrix formulation (equation 5.30) can be interpreted as to consider the total MMF distribution as a superposition of MMF distributions of particular slots. 

The idea of rotational symmetry exploitation is to nd out a set of vectors: 

$$
\mathbb {U} _ {\overline {{\boldsymbol {c}}}} = \left\{\overline {{\boldsymbol {c}}} _ {0}, \overline {{\boldsymbol {c}}} _ {1}, \dots , \overline {{\boldsymbol {c}}} _ {N _ {u}} \right\} \tag {5.49}
$$

so that: 

$$
\overline {{\boldsymbol {c}}} _ {k} = \mathbf {S} ^ {\mathrm{R}} \cdot \overline {{\boldsymbol {c}}} _ {h}, \quad \begin{array}{c} k = 0 \dots m - 1 \\ \overline {{\boldsymbol {c}}} _ {h} \in \mathbb {U} _ {\overline {{\boldsymbol {c}}}} \end{array} \tag {5.50}
$$

where $\mathbf { S } ^ { \mathrm { R } }$ is a $N _ { s } \times N _ { s }$ transformation matrix with the element is dened as: 

$$
s _ {n, k} ^ {\mathrm{R}} = \left\{ \begin{array}{l l} 1 & , k = \operatorname{mod} (n + g, N _ {s}) \\ 0 & , \text { else } \end{array} \right. \tag {5.51}
$$

where g is an integer within the interval $1 < g < N _ { s }$ . 

For the normalized conductor distribution matrix with rotational symmetry, the number of normalized conductor distribution vector is then reduced. In most cases where the topology of all phase windings are the same, there is only one element within the set $\mathbb { U } _ { \overline { { c } } }$ . Physically, the set $\mathbb { U } _ { \overline { { c } } }$ gives the information about how many unique primitive phase winding topologies under consideration of rotational symmetry are available for the primitive multi-phase winding. 

From gure 5.9, it is to observe that by considering the rotational symmetry, the topology of each phase winding is the same. Therefore, for both cases, there is only one unique normalized conductor distribution vector. 

For winding topologies with rotational symmetry, equation 5.48 is then reduced to: 

$$
\overline {{\boldsymbol {\Theta}}} = \sum_ {h = 0} ^ {N _ {u}} \underline {{\phi}} _ {k} \cdot \mathbf {S} _ {k, h} ^ {\mathrm{R}} \cdot \overline {{\boldsymbol {c}}} _ {h} \tag {5.52}
$$

The rotational symmetry simplies the further analysis of the topology within the unique normalized conductor distribution vectors since the topology of the total multi-phase winding is just a symmetrical construction of them. 

Without losing the generality, it is necessary to consider only one of the unique normalized conductor distribution vectors for the further discussion, since the analysis process is the same for the other vectors. To make the mathematical notation of the further discussion clear, notation $\overline { { c } } ^ { \mathrm { R } }$ is assigned to the considered unique normalized conductor distribution vector. 

The unique normalized conductor distribution vector is also termed as primitive phase winding in this thesis. 

# 5.4.6.2. Mirror symmetry: the symmetry within the primitive phase winding

If there exists an integer g of $0 \leq g < N _ { s }$ , so that the unique normalized conductor distribution vector $\overline { { c } } ^ { \mathrm { R } }$ is invariant to the following transformation: 

$$
\overline {{\boldsymbol {c}}} ^ {\mathrm{R}} = \mathbf {S} ^ {\mathrm{M}} \cdot \overline {{\boldsymbol {c}}} ^ {\mathrm{R}} \tag {5.53}
$$

where $\mathbf { S } ^ { \mathrm { M } }$ is a $N _ { s } \times N _ { s }$ matrix with: 

$$
s _ {n, k} ^ {\mathrm{M}} = \left\{ \begin{array}{l l} 1, & , n = \operatorname{mod} (g - k, N _ {s}) \\ 0, & , \text { else } \end{array} \right. \tag {5.54}
$$

Then there is mirror symmetry within the primitive phase winding topology, where g indicates the position of the symmetrical axis. Analysis of this number shows that an even number of g means that the symmetrical axis lies in the middle of a slot; an odd number of g means that the symmetrical axis lies in the middle of a tooth. This is illustrated in gure 5.10a for $g = 1 0$ and gure 5.10b for $g = 1$ respectively. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/fe8f877be071466c5d857f56e09778346e8aebce51713eef9cf83eeca524f47b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/55f009f34c466a5b9b249dcbb6616d9e42199ffddc1a3c91e7bcd4c03fb27643.jpg)



(a) Symmetry axis through middle of a (b) Symmetry axis through middle of a slot tooth



Figure 5.10.: The mirror symmetry of the primitive phase winding topology


After the mirror symmetry is detected, the normalized conductor distribution vector $\overline { { c } } ^ { \mathrm { R } }$ can be rewritten as: 

$$
\overline {{{c}}} ^ {\mathrm{R}} = \overline {{{c}}} ^ {\mathrm{R}, \mathrm{M}} + \mathbf {S} ^ {\mathrm{M}} \cdot \overline {{{c}}} ^ {\mathrm{R}, \mathrm{M}} \tag {5.55}
$$

where $\overline { { c } } ^ { \mathrm { R , M } }$ represents one part of the primitive phase winding topology besides the symmetry axis and is termed as primitive coil group. 

To obtain the upper as well as the lower mirror symmetry part of $\overline { { c } } ^ { \mathrm { R } }$ , equation 5.55 is changed to: 

$$
\begin{array}{l} \overline {{{\boldsymbol {c}}}} ^ {\mathrm{R}} = \mathbf {S} ^ {\mathrm{M}, \mathrm{u}} \cdot \overline {{{\boldsymbol {c}}}} ^ {\mathrm{R}, \mathrm{M}, \mathrm{u}} \\ - \overline {{{\boldsymbol {r}}}} ^ {\mathrm{R}} = \mathbf {s} ^ {\mathrm{M}, \mathrm{l}} - \overline {{{\boldsymbol {r}}}} ^ {\mathrm{R}, \mathrm{M}, \mathrm{l}} \end{array} \tag {5.56}
$$

$$
\overline {{\boldsymbol {c}}} ^ {\mathrm{R}} = \mathbf {S} ^ {\mathrm{M,l}} \cdot \overline {{\boldsymbol {c}}} ^ {\mathrm{R,M,l}}
$$

with: 

$$
\begin{array}{l} \mathbf {S} ^ {\mathrm{M}, \mathrm{u}} = \mathbf {I} + \mathbf {S} _ {:, \mathrm{mod} (\boldsymbol {k} ^ {\mathrm{u}}, N)} ^ {\mathrm{M}} \\ \mathbf {S} ^ {\mathrm{M}, 1} = \mathbf {I} + \mathbf {S} ^ {\mathrm{M}} \end{array} \tag {5.57}
$$

$$
\mathbf {S} ^ {\mathrm{M}, \mathrm{l}} = \mathbf {I} + \mathbf {S} _ {:, \mathrm{mod} (\boldsymbol {k} ^ {\mathrm{l}}, N)} ^ {\mathrm{M}}
$$

where the indices are dependent on whether g is an even or odd number, which are calculated as: 

$$
\boldsymbol {k} ^ {\mathrm{u}} = \left\{ \begin{array}{l l} \text {arange} \left(\text {ceil} \left(\frac {g}{2}\right), \text {int} \left(\frac {N _ {s}}{2}\right)\right) & g: \text {is odd} \\ \text {arange} \left(\text {ceil} \left(\frac {g}{2}\right), \text {int} \left(\frac {N _ {s}}{2}\right) + 1\right) & g: \text {is even} \end{array} \right. \tag {5.58}
$$

$$
\pmb {k} ^ {\mathrm{l}} = \pmb {k} ^ {\mathrm{u}} + \mathrm{int} \left(\frac {N _ {s}}{2}\right)
$$

where the function arange $( a , b )$ returns a $1 \times b$ vector starting from a with increment of 1. 

Solving equation 5.56 gives the topology of the upper and lower primitive coil groups respectively: 

$$
\overline {{{c}}} ^ {\mathrm{R}, \mathrm{M}, \mathrm{u}} = \left(\mathbf {S} ^ {\mathrm{M}, \mathrm{u}}\right) ^ {- 1} \cdot \overline {{{c}}} ^ {\mathrm{R}} \tag {5.59}
$$

$$
\overline {{\boldsymbol {c}}} ^ {\mathrm{R,M,l}} = \left(\mathbf {S} ^ {\mathrm{M,l}}\right) ^ {- 1} \cdot \overline {{\boldsymbol {c}}} ^ {\mathrm{R}}
$$

Because of the mirror symmetry, for the further discussion, it needs only to consider one of the mirror symmetry part, which is assigned with the notation of $\overline { { c } } ^ { \mathrm { R , M } }$ and $\mathbf { S } ^ { \mathrm { M } }$ for clarity. 

Equation 5.52 is then: 

$$
\overline {{{{\boldsymbol {\Theta}}}}} = \sum_ {h = 0} ^ {N _ {u}} \underline {{{{\phi}}}} _ {k} \cdot \mathbf {S} _ {k, h} ^ {\mathrm{R}} \cdot \mathbf {S} _ {k, h} ^ {\mathrm{M}} \cdot \overline {{{{\boldsymbol {c}}}}} _ {h} ^ {\mathrm{R}, \mathrm{M}} \tag {5.60}
$$

which describes how the primitive multi-phase winding is constructed by the primitive coil group through symmetry transformation. 

# 5.4.7. Connection of the conductors of the primitive coil group: the primitive coils

Once the primitive coil group is obtained, the next step is to consider how to connect the conductors within the primitive coil group to coils. The connections should be so chosen that the resulting coils approximate the primitive coil group as good as possible. This depends on the design constraints, which can be categorized into three main types and lead to winding topologies of dierent complexity. 

For the discussion, it is assumed that the total number of the conductor distributions within the primitive coil group is $N _ { \overline { { c } } } ,$ , which is the number of the non-zero elements of the vector $\overline { { c } } ^ { \mathrm { R , M } }$ . The number of the positive conductor distribution is $N _ { \overline { { c } } , p }$ and the number of the negative conductor distributions is then $N _ { \overline { { c } } , n }$ . There is: 

$$
N _ {\overline {{c}}} = N _ {\overline {{c}}, p} + N _ {\overline {{c}}, n} \tag {5.61}
$$

where $N _ { \overline { { c } } , p }$ is not necessary equal to $N _ { \overline { { c } } , n }$ . For the case of $N _ { \overline { c } , p } \neq N _ { \overline { c } , n } .$ , $N _ { \overline { { c } } , s }$ is used to describe the smaller number of them. 

Furthermore, it is assumed that the connection is only between positive and negative conductor distributions. Each connection is mathematically formulated as a $N _ { s } \times 1$ vector $m _ { c }$ with two non-zero elements of +1 and 1. The position of the non-zero element indicates the position of the positive or negative conductor distribution within the primitive coil group $\bar { \pmb { c } } ^ { \mathrm { R , M } }$ 

$$
m _ {c, n} = \left\{ \begin{array}{l l} \operatorname{sign} \left(\overline {{c}} _ {n} ^ {\mathrm{R}, \mathrm{M}}\right), & n = n _ {p}, n _ {n} \\ 0, & n \neq n _ {p}, n _ {n} \end{array} \right. \tag {5.62}
$$

Such connection is called as primitive coil in this thesis since it denes only a part of the properties of a coil, which are: 

 the coil pitch: 

$$
\tau_ {c} = \text { CoilPitch } \left(\boldsymbol {m} _ {c}\right) \tag {5.63}
$$

 the position of the coil: 

$$
\beta_ {c} = \operatorname{Posi} \left(\boldsymbol {m} _ {c}\right) \tag {5.64}
$$

The third property of a coil: the number of turns $w _ { c }$ , depends on the design constraints and will be discussed later. 

The total $N _ { x }$ connections together can be formulated as a matrix, with each connection as its column vector. Such matrix is called as connection matrix in this thesis: 

$$
\mathbf {M} _ {c} = \left[ \begin{array}{l l l l l} \boldsymbol {m} _ {c, 0} & \boldsymbol {m} _ {c, 1} & \boldsymbol {m} _ {c, 2} & \dots & \boldsymbol {m} _ {c, N _ {x} - 1} \end{array} \right] \tag {5.65}
$$

# 5.4.7.1. The double-way connection approach

The double-way connection fullls the following constraints: 

 Each conductor distribution is connected with two conductor distributions of opposite winding direction, 

 The path of the total connections is the shortest among the possible connections. 

Under these constraints, there are total $2 N _ { \overline { { c } } , s }$ s connections, which can be formulated as a connection matrix $\mathbf { M } _ { c } ^ { \mathrm { D } }$ . This double-way connection matrix represents a 4-layer winding topology with coils of dierent coil pitch and number of turns. Such winding topology is the design basis of the multi-layer and multi-turn winding topology. 

An example of the double-way connections of a primitive coil group (gure 5.11a) is given in gure 5.11b. Each conductor distribution (illustrated by the lime circles) is assigned with two connections (illustrated by the dark bold lines). There are total four primitive coils where 3 of them are having coil pitch of 1 slot pitch, and 1 of them is having coil pitch of 3 slot pitch. 

# 5.4.7.2. The single-way connection approach

Another approach to connect the conductor distributions is the singleway connection. By using the single-way connection, each conductor distribution is assigned to one connection. This leads to totally $N _ { \overline { { c } } , \ast }$ s connections and results in a double-layer winding topology. 

Two dierent types of single-way connection are considerable. They are the single-way connection of shortest path (gure 5.11c) and the singleway connection of minimum deviation (gure 5.11d). 

The shortest path connection If each connection is considered as a coil, the single-way connection of shortest path is to realize the winding with coils of possible short coil pitch, so that sum of the total coil pitch is minimal: 

$$
\sum \tau_ {c} \rightarrow \min \tag {5.66}
$$

Mathematically, this is the shortest path problem and is inecient to solve. Thanks to the symmetry consideration, all the practice relevant problems dealt can be reduced to a small scope, so that it possible to use a normal desktop computer to check all the combinations in a quite short time. 

As an example, design of a 3-phase winding with 120 slots is considered. After exploiting the rotational and mirror symmetry of the winding topology, the number of conductor distributions of the primitive coil group is reduced to: $N _ { \overline { { c } } } = 1 2 0 \div 3 \div 2 = 2 0$ . The number of the positive and negative conductor distributions are: $N _ { \overline { { c } } , p } = N _ { \overline { { c } } , n } = N _ { \overline { { c } } } \div 2 = 1 0$ that results in a total number of combinations: $N _ { x } = 1 0 ! = 3 , 6 2 8 , 8 0 0$ . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/989492f99a4d1698582d933cf2c118e13a564742c6e61193b94e13de8df15629.jpg)



(a) The conductor distributions within a primitive coil group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/fa0c6760b8d8e1a0903edab0940e56159c098364f630280cb4183de56ebf2d9e.jpg)



(b) The double-way connections


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/9003b10fb48d4b1d8a6363dce002a50e25fbd8e5ed6327968034e95863974408.jpg)



(c) The single-way connections of shortest path


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/4c3e83f29778150b944cc29e8225bd4414ea63839b1b9721c95d91cd3cce4a73.jpg)



(d) The single-way connections of minimum deviation



Figure 5.11.: The conductor distributions within a primitive coil group and the corresponding double- and single-way connections


Once the shortest path connection is known, a $N _ { s } \times N _ { \overline { { c } } , s }$ connection matrix $\mathbf { M } _ { c } ^ { \mathrm { S } , \mathrm { S P } }$ can be obtained, which builds the design basis of the multiconductor winding topology. 

The minimal deviation connection The conductor deviation of a coil is dened as the deviation between the number of the positive and the negative conductor distributions. In the minimum deviation connection, it is to realize the winding topology with coils of possible small conductor deviation, so that sum of the total conductor deviation is minimal: 

$$
\sum \left| N _ {c, p} - N _ {c, n} \right|\rightarrow \min \tag {5.67}
$$

This leads to another type of $N _ { s } \times N _ { \overline { { c } } , s }$ connection matrix $\mathbf { M } _ { c } ^ { \mathrm { S , M D } }$ , which builds the design basis of the multi-coil winding topology. 

# 5.4.8. Derivation of the winding topology

# 5.4.8.1. Design of the multi-turn winding topology

The multi-turn winding topology is characterized through: 

 Each slot is with multiple coil sides, 

 All the coils have equal coil pitch, 

 The number of turns per coil may be dierent. 

Such winding topology can be easily derived through the double-way connection matrix $\mathbf { M } _ { c } ^ { \mathrm { D } }$ . This is done by nding out the connections $m _ { c } ^ { \mathrm { M T } }$ having the same coil pitch $\tau _ { c } ^ { * }$ : 

$$
\text { CoilPitch } \left(\boldsymbol {m} _ {c} ^ {\mathrm{MT}}\right) = \tau_ {c} ^ {*}, \quad \boldsymbol {m} _ {c} ^ {\mathrm{MT}} \in \mathbf {M} _ {c} ^ {\mathrm{D}} \tag {5.68}
$$

which result in a connection matrix $\mathbf { M } _ { c } ^ { \mathrm { M T } }$ of possible large rank number: 

$$
N _ {c} = \operatorname{rank} \left(\mathbf {M} _ {c} ^ {\mathrm{MT}}\right)\rightarrow \max \tag {5.69}
$$

If each connection is considered as a coil with an unknown number of turns $w _ { c } ,$ , a system of linear equations with $N _ { c }$ equations can be formulated: 

$$
\mathbf {M} _ {c} ^ {\mathrm{MT}} \cdot \boldsymbol {w} _ {c} ^ {\mathrm{MT}} = \overline {{\boldsymbol {c}}} ^ {\mathrm{R}, \mathrm{M}} \tag {5.70}
$$

Generally, the obtained system of linear equations is over-determined, since rank $\left( \mathbf { M } _ { c } ^ { \mathrm { M T } } \right) < \mathrm { r a n k } \left( \mathbf { \bar { M } } _ { c } ^ { \mathrm { D } } \right) \leq N _ { \overline { { c } } }$ . This means no solution is available. Nevertheless, a best approximation with respect to the least squares can be obtained: 

$$
\boldsymbol {w} _ {c} ^ {\mathrm{MT}} = \left(\left(\mathbf {M} _ {c} ^ {\mathrm{MT}}\right) ^ {\mathrm{T}} \mathbf {M} _ {c} ^ {\mathrm{MT}}\right) ^ {- 1} \cdot \left(\mathbf {M} _ {c} ^ {\mathrm{MT}}\right) ^ {\mathrm{T}} \cdot \overline {{\boldsymbol {c}}} ^ {\mathrm{R}, \mathrm{M}} \tag {5.71}
$$

The error caused due to the approximation is then calculated as: 

$$
\epsilon^ {\mathrm{MT}} = \mathbf {M} _ {c} ^ {\mathrm{MT}} \cdot \pmb {w} _ {c} ^ {\mathrm{MT}} - \overline {{\pmb {c}}} ^ {\mathrm{R,M}} (5. 7 2)
$$

which is used to calculate the relative error : 

$$
\epsilon^ {\mathrm{MT}} = \frac {\mathrm{norm} (\epsilon^ {\mathrm{MT}} , 2)}{\mathrm{norm} (\overline {{c}} ^ {\mathrm{R,M}} , 2)} \tag {5.73}
$$

where the function norm (x, 2) calculates the 2  norm of a vector x. 

An example of the multi-turn winding topology is given in gure 5.12a which is derived from the double-way connection shown in 5.11b. In this special case, the multi-turn winding topology exactly reconstructs the primitive coil group. This means no error is caused by the least squares approximation. 

# 5.4.8.2. Design of the multi-layer winding topology

The multi-layer winding topology can be seen as a special case of the multi-turn winding topology where the coils are with the same number of turns. Therefore, the multi-layer winding topology can be derived by normalizing the solution wMTc (obtained in equation 5.71) by its minimal ${ \pmb w } _ { c } ^ { \mathrm { M T } }$ element min $\left( \pmb { w } _ { c } ^ { \mathrm { M T } } \right)$ and then rounding the elements of the vector to the nearest integer: 

$$
\boldsymbol {w} _ {c} ^ {\mathrm{ML}} = \operatorname{rint} \left(\frac {\boldsymbol {w} _ {c} ^ {\mathrm{MT}}}{\min \left(\boldsymbol {w} _ {c} ^ {\mathrm{MT}}\right)}\right) \cdot \min \left(\boldsymbol {w} _ {c} ^ {\mathrm{MT}}\right) \tag {5.74}
$$

An example of the multi-layer winding topology is given in 5.12b which is derived from the multi-turn winding topology shown in gure 5.12a. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/c997158bd66da535a69998ab925fb7d66af2919cc7eb5db771af6080f40b48e3.jpg)



(a) Derivation of the multi-turn winding topology from the double-way connection given in gure 5.11b


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/7dde458af8dccb101a32230119ffa6fe3e64962188f697f1f60eb1d78248ccb9.jpg)



(b) Derivation of the multi-layer winding topology from the multi-turn winding topology in the left



Figure 5.12.: Derivation of multi-turn and multi-layer winding topology


# 5.4.8.3. Design of the multi-coil winding topology

The multi-coil winding topology is derived from the single-way connection of minimal deviation. The connection matrix $\mathbf { M } _ { c } ^ { \mathrm { S , \bar { M D } } }$ is used for the calculation of the number of turns ${ \pmb w } _ { c } ^ { \mathrm { M C } }$ : 

$$
\mathbf {M} _ {c} ^ {\mathrm{S}, \mathrm{MD}} \cdot \boldsymbol {w} _ {c} ^ {\mathrm{MC}} = \overline {{\boldsymbol {c}}} ^ {\mathrm{R}, \mathrm{M}} \tag {5.75}
$$

Solving equation above by using the least squares method results in a winding topology with coils of dierent coil pitch and number of turns. An example of the multi-coil winding topology is given in 5.13 which is derived from the single-way connection of minimal derivation shown in gure 5.11d. 

# 5.4.8.4. Design of the multi-conductor winding topology

As discussed in section 4.3.2.4, due to the constraint of one coil side having one conductor more than the other coil side, there is only one optimal solution for the number of conductors of the multi-conductor winding topology. In contrast, the previous winding topologies are independent on the total number of conductors. This makes the determination of the number of conductors per coil side of the multi-conductor winding topology dierent from the previous winding topologies. Nevertheless, the connection matrix of the single-way connection of shortest path $\mathbf { M } _ { c } ^ { \mathrm { S , S P } }$ is used for the calculation of the number of conductors $N _ { c } ^ { \mathrm { M C o n d } }$ . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/242d70b58c4b8a28f403c9bb79147bb6805d48458bf829e13b00222de6beb78f.jpg)



(a) Derivation of the multi-coil winding topology from the single-way connection of minimal deviation shown in gure 5.11d


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a608e6743638e3defd8e3322ba64496e4caf2e2e78c1efb606189156b10a6257.jpg)



(b) Derivation of the multi-conductor winding topology from the single way connection of shortest path shown in gure 5.11c



Figure 5.13.: Derivation of the multi-coil and multi-conductor winding topology


For the discussion, the number of conductors of the negative coil side is considered as unknown $N _ { c } ^ { \mathrm { M C o n d } }$ . Furthermore, two vectors $\mathbfit { n _ { p } }$ and $\mathbf { \delta } _ { \mathbf { \eta } ^ { n } }$ are dened for the positions of the positive and negative coil sides of the connection matrix $\mathbf { M } _ { c } ^ { \mathrm { S } , \mathrm { S P } }$ . The winding design is then considered as to determine a ratio a and the unknown number of conductors of the negative coils side N MCond, $N _ { c } ^ { \mathrm { M C o n d } }$ so that: 

$$
a \cdot N _ {c} ^ {\mathrm{MCond}} = \overline {{\boldsymbol {c}}} _ {\boldsymbol {n} _ {n}} ^ {\mathrm{R,M}}
$$

$$
a \cdot \left(\boldsymbol {N} _ {c} ^ {\mathrm{MCond}} + \boldsymbol {m} ^ {\mathrm{Mcond}}\right) = \overline {{\boldsymbol {c}}} _ {\boldsymbol {n} _ {p}} ^ {\mathrm{R}, \mathrm{M}} \tag {5.76}
$$

where the $N _ { s } \times 1$ column vector $m ^ { \mathrm { M c o n d } }$ is dened as: 

$$
m _ {n} ^ {\text { Mcond }} = \left\{ \begin{array}{l l} \text { sign } \left(\overline {{\boldsymbol {c}}} _ {\boldsymbol {n} _ {p}} ^ {\text { R,M }} + \overline {{\boldsymbol {c}}} _ {\boldsymbol {n} _ {n}} ^ {\text { R,M }}\right) & n = n _ {p}, n _ {n} \\ 0 & n \neq n _ {p}, n _ {k} \end{array} \right. \tag {5.77}
$$

By introducing two intermediate variables: 

$$
\begin{array}{l} \boldsymbol {x} = a \cdot \boldsymbol {N} _ {c} ^ {\mathrm{MCond}} \tag {5.78} \\ y = a \\ \end{array}
$$

A system of linear equations with $N _ { s }$ equations and $N _ { c } + 1$ unknowns (the rst $N _ { c }$ unknowns for x and the last unknown for y) is obtained: 

$$
\mathbf {M} ^ {\mathrm{MCond}} \cdot \left[ \begin{array}{c} \boldsymbol {x} \\ y \end{array} \right] = \overline {{\boldsymbol {c}}} ^ {\mathrm{R}, \mathrm{M}} \tag {5.79}
$$

where the matrix MMCond is dened as: 

$$
\mathbf {M} ^ {\mathrm{MCond}} = \left[ \begin{array}{c c} \mathbf {M} _ {c} ^ {\mathrm{S}, \mathrm{SP}} & \boldsymbol {m} ^ {\mathrm{Mcond}} \end{array} \right] \tag {5.80}
$$

Solving equation 5.79 by using the least squares method gives the intermediate variables x and $y ,$ which are used for the calculation of $N _ { c } ^ { \mathrm { M C o n d } }$ . Since the number of conductors should be an integer, a round-o towards the nearest integer is applied, leading to: 

$$
\boldsymbol {N} _ {c} ^ {\mathrm{MCond}} = \operatorname{rint} \left(\frac {\boldsymbol {x}}{y}\right) \tag {5.81}
$$

Unlike the method introduced in [20], where the optimal number of conductors is obtained by trying to modify an existing winding topology. In this thesis, the optimal number of conductors is found by directly solving the system of linear equations 5.79. 

# 5.4.8.5. Design of the double-layer winding topology

The double-layer winding topology is dened as the number of coil sides within each slot is two. It can be easily derived from the single-way connection, which is a double-layer winding topology in nature. 

Both types of connection matrix can be used, leading to winding topologies of dierent geometrical conguration but generally with the same electromagnetic property. This is due to the strong constraint that the coils are having the same number of turns: 

$$
\mathbf {M} _ {c} ^ {\mathrm{CD}} = \mathbf {M} _ {c} ^ {\mathrm{S}} \tag {5.82}
$$

where the connection matrix $\mathbf { M } _ { c } ^ { \mathrm { S } }$ can be $\mathbf { M } _ { c } ^ { \mathrm { S } , \mathrm { S P } }$ or $\mathbf { M } _ { c } ^ { \mathrm { S , M D } }$ 

In order to guarantee that all the coils are having the same number of turns, the system of linear equations used for the determination of the number of turns degenerates to: 

$$
\pmb {m} ^ {\mathrm{CD}} \cdot w _ {c} ^ {\mathrm{CD}} = \overline {{\pmb {c}}} ^ {\mathrm{R,M}} \tag {5.83}
$$

which is a system of $N _ { s }$ linear equations and has only one unknown. The $N _ { s } \times 1$ vector $m ^ { \mathrm { C D } }$ is calculated from the connection matrix $\mathbf { M } _ { c } ^ { \mathrm { C D } }$ through: 

$$
\boldsymbol {m} ^ {\mathrm{CD}} = \operatorname{sum} \left(\mathbf {M} _ {c} ^ {\mathrm{CD}}, \text {axis} = 1\right) \tag {5.84}
$$

where the function sum (A, axis = 1) does a sum over the rows, resulting in a $N _ { s } \times 1$ vector a. 

Up on solving the over-determined system of linear equations 5.83 using the least squares method gives the searched number of turns for all the coils $w _ { c } ^ { \mathrm { C D } }$ . Two examples of the double-layer winding topology are given in 5.14 which are derived from the single-way connection of shortest path and minimal deviation. 

# 5.4.8.6. Design of the single-layer winding topology

The single-layer winding topology is dened as the number of coil sides within each slot is one. It can be seen as a special case of the double-layer winding topology. This can be done by remove one conductor distribution of the primitive double-layer winding topology from each slot. 

To determine which conductor distribution should be removed from the particular slot, the number of conductors of each conductor distribution is used to measure the importance of the conductor distribution. After removing the conductor distribution with smaller number of conductors, a primitive single-layer winding topology $\overline { { \mathbf { C } } } _ { s }$ is obtained: 

$$
\overline {{c}} _ {s, n, k} = \left\{ \begin{array}{l l} \overline {{c}} _ {n, k _ {0}} & k = k _ {0} \\ 0 & k \neq k _ {0} \end{array} \right. \tag {5.85}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/292fd2826754675f2b44485e2ff4ead84af1160ba9d6c21eb69220a182d732ec.jpg)



(a) Derivation of the double-layer winding topology from the single-way connection of shortest path given in gure 5.11c


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/f6e20a9b7c1ee30b62bf9def9726f792679566812cd854a817fcbe7aad879201.jpg)



(b) Derivation of the Double-layer winding topology from the single-way connection of minimal deviation - gure 5.11d



Figure 5.14.: Derivation of the double-layer winding topology


where 

$$
k _ {0} = \operatorname{argmax} (\overline {{\boldsymbol {c}}} _ {n}) \tag {5.86}
$$

After exploiting the symmetry properties (section 5.4.6), a primitive single-layer coil group $\overline { { \pmb { c } } } _ { s } ^ { \mathrm { R , M } }$ can be obtained. Under the same consideration, the single-way connection of shortest path $\mathbf { M } _ { c , s } ^ { \mathrm { S } , \mathrm { S P } }$ as well as minimal deviation MS,MD $\mathbf { M } _ { c , s } ^ { \mathrm { S , M D } }$ can be obtained for the primitive coil group single-layer. 

Once the single-way connection matrix is obtained, the same technique used in section 5.4.8.5 for the double-layer winding topology is applied to guarantee that all the coils have the same number of turns: 

$$
\boldsymbol {m} ^ {\mathrm{CS}} \cdot w _ {c} ^ {\mathrm{CS}} = \overline {{\boldsymbol {c}}} ^ {\mathrm{R}, \mathrm{M}} \tag {5.87}
$$

with: 

$$
\boldsymbol {m} ^ {\mathrm{CS}} = \operatorname{sum} \left(\mathbf {M} _ {c} ^ {\mathrm{CS}}, \text { axis } = 1\right) \tag {5.88}
$$

An example of the single-layer winding topology is given in gure 5.15 which shows how the primitive single-layer coil group (gure 5.15a) is derived from the primitive double-layer coil group (gure 5.11a) and how the single-layer winding topology (gure 5.15b) is derived from the primitive single-layer coil group by using single-way connections. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/3944b951bba1094cf0832d9a85da5a14af5478a05c37f3d398026a8abb56fbdc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2602934172c5e90b52fb5bb21b4ebb3391c4d799278f78515834841e3d75d875.jpg)



(a) Derivation of the primitive singlelayer coil group from the primitive double-layer coil group given in - gure 5.11a



(b) Derivation of the single-layer winding topology from the primitive single-layer coil group in the left



Figure 5.15.: Derivation of the single-layer winding topology


# 5.4.9. Evaluation of the winding topology: calculation of the winding factor harmonic spectrum

After various winding topologies are obtained, it is the last step to evaluate the electromagnetic performance of each winding topology by calculating its winding factor harmonic spectrum. 

This is performed in 2 steps. It starts from the coils of the coil group and goes in the inverse direction of the winding design procedures: 

 Calculate the real normalized MMF distribution of the winding topology by applying the mirror symmetry and rotational symmetry to the coils (equation 5.52), 

 Calculate the real winding factor harmonic spectrum from the real normalized MMF distribution by using equation 5.31. 

The proposed method guarantees that all the obtained winding topologies under the given constraints are with optimal winding factor harmonic spectrum. This means that the working harmonic is with a large winding factor and the sub- and over-harmonics are with small winding factors. To better illustrate and compare the results, the deviation of the actual winding factor harmonic spectrum of each obtained winding topology from the optimal winding factor harmonic spectrum is shown and discussed. 

The evaluation results of the winding topologies obtained in the previous subsections (from gure 5.12 to 5.15) are given in gure 5.16. It is observed that a complete elimination of the sub-harmonics contents of the discussed over-harmonic winding topology is possible by using: 

 The multi-turn winding topology, which is a triple-layer winding with coils of same coil pitch and two dierent number of turns (gure 5.16a), 

 The multi-coil winding topology, which is a double-layer winding with coils of two dierent coil pitches and number of turns (gure 5.16c). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/637b1126eeeecc38a2fa6da2b64c9b2604c3be80c14237bd67bd1bd6047a6c88.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2dadce547439f3d49208cb06b9aa9dea51ca0bb92aa564a9dde99b4df3df946d.jpg)



(a) The multi-turn winding topology: the coil group (left) and the deviation of the winding factor harmonic spectrum (right)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/b6160287920a4650df3aebc2dad59ebb447818de1e905923a2b6047cadfcbc1f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/050d6921b1c1322d0778f760a5704b2241be4517b06b003735487a315500eb7f.jpg)



(b) The multi-layer winding topology: the coil group (left) and the deviation of the winding factor harmonic spectrum (right)



Figure 5.16.: Evaluation of the winding topology


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/1ff74c49e79db6a61f562c642c4ae31b8644b7faae0a756e796422c330ba8413.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/0177e8dff83e5679b5df1ccaddcc110171dcaea885964af8cf07cce85eee8f0c.jpg)



(c) The multi-coil winding topology: the coil group (left) and the deviation of the winding factor harmonic spectrum (right)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/ea3b64e817c8dbd17ad96bfb7f69d6d7248d4af3e3f2782d6518a40ff998d393.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/47d84ff755c87cad25a90527ac41bddd310c67f9f1eb1053af7d7dcb11cb69ae.jpg)



(d) The multi-conductor winding topology: the coil group (left) and the deviation of the winding factor harmonic spectrum (right)



Figure 5.16.: Evaluation of the winding topology


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/db5e807d968181e41a3aac4896dc49edfd50709a511ddf6ef47f994c4d7d2910.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/3498def1d554fcafe232f11809863a933bd134ea34b207775a799d0f674b9ace.jpg)



(e) The classical double-layer winding topology derived from the single-way connection of shortest path: the coil group (left) and the deviation of the winding factor harmonic spectrum (right)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/c194e01c45a4e47a84875ba82d1d324d49e531aad867ecace8a725b1dc43b544.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/df8c2e133f7781b1b5c1a53e52a4598c846d56b42c1e23e91519c0367718c859.jpg)



(f) The classical double-layer winding topology derived from the single-way connection of minimal deviation: the coil group (left) and the deviation of the winding factor harmonic spectrum (right)



Figure 5.16.: Evaluation of the winding topology


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/d4459eb57681c3dbabb985363a07c3d0981eab1636027327e450661f7bcb835b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/3a34031e621a240daf243ac6ac0f5e7837e296ac938ef5e0f50e875308b4f897.jpg)



(g) The classical single-layer winding topology derived from the primitive single-layer coil group: the coil group (left) and the deviation of the winding factor harmonic spectrum (right)


Figure 5.16.: Evaluation of the winding topology 

# 6. Application of the proposed method for the treatment of winding topology

Three examples are given to show how to embed the introduced method into the winding topology design procedures. The examples that are chosen is based on the following considerations: 

 It should cover a wide range of case studies to show the ability of the introduced method. Designs of fundamental and over-harmonic winding topologies with odd and even number of phases and odd and even number of slots are then chosen. 

 It should be possible to validate the results. The examples are so chosen that they are possible to compare with those from the literature. 

Based on these criteria, a step by step design approach of the wellknown 3-phase winding of 12 slots with working harmonics of $\gamma = 1$ and $\gamma = 5$ is discussed in detail. Later on, an example of 3-phase winding of 9 slots with working harmonic of $\gamma = 4$ is given in a more general way, showing the ability of the method for treating winding topology with an odd number of slots. Finally, an example of a 6-phase winding having 24 slots with working harmonic of $\gamma = 5$ is given, showing the ability of the method for treating winding topology with an even number of phases. 

A comprehensive comparison of the obtained winding topologies with those from various textbooks and publications is given, showing the validity and generality of the method. 

Furthermore, a class of winding topologies, which is according to the author's knowledge entirely new, is given and discussed, showing the novelty of the method. 

# 6.1. The 3-phase fundamental and over-harmonic winding of 12 slots

# 6.1.1. The design procedure

To be considered are two winding topologies with working harmonic of γ = 1 and γ = 5. For the both windings, the number of phase is 3 and the number of slots is 12 (gure 6.1). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/84a0ef101895da023048c3b7f7b918c3ae11a511df0cff1be94e5e11458c1435.jpg)



(a) Symmetrical 3-phase current system


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/4843da9b82af19575454484c56ac4e11f04a8f94a3e8475292cbf84a15782a6f.jpg)



(b) Stator with 12 slots



Figure 6.1.: The design parameters


# 6.1.1.1. The ideal winding factor harmonic spectrum

The rst step of the design procedures is to dene the ideal winding factor harmonic spectrum, which can be obtained according to equation 5.37 and is shown in gure 6.2 for the fundamental and over-harmonic winding respectively. 

# 6.1.1.2. The ideal normalized MMF distribution

After the ideal winding factor harmonic spectrum is dened, the ideal normalized MMF distribution can be calculated by using equation 5.38. 

The MMF phasor of the n-th slot is calculated by using equation 5.39. The results are shown in gure 6.3 for the fundamental and over-harmonic winding respectively. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/52d654bf88f9d64013ca6de0751116b97177221fe2813245768f038f3ecea6e3.jpg)



(a) Working harmonic of $\gamma = 1$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/8135ed8d2d72c5f6a3ee53a9d067904e9c2e64f5bf5f43935fb0aeb05481e848.jpg)



(b) Working harmonic of $\gamma = 5$



Figure 6.2.: The ideal winding factor harmonic spectrum


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/0cdf10f2310846e1b5e7370fe2a7b376a11d0ab25e22dfcc2ebabfe85e5c7148.jpg)



(a) Working harmonic of $\gamma = 1$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/982d5c266b2cab860be608b5c433187cc9d13e4a4f1b68026cf0b11c9335488c.jpg)



(b) Working harmonic of $\gamma = 5$



Figure 6.3.: The ideal normalized MMF distribution


# 6.1.1.3. The normalized conductor distribution matrix and the primitive double-layer multiphase winding

After the ideal MMF distribution is dened, the next step is to determine the phase aliation of the conductors within each slot by using equation 5.44 and to calculate the normalized number of conductors within each slot by using equation 5.46. 

The Result of this design procedure is the normalized conductor distribution matrix, which can be interpreted as a primitive double-layer winding with each slot of a dierent number of conductors belonging to dierent phases. 

The normalized conductor distribution matrices of the both investigated winding topologies are shown from gure 6.4 to 6.7 respectively. Dierent graphical presentation forms are used to illustrate the winding topologies. 

As mentioned in the previous chapter, dierent types of normalized conductor distribution matrix can be obtained, depending on the angle oset between the multiphase current system and the ideal normalized MMF distribution. 

For the both investigated winding topologies, there are two types of normalized conductor distribution matrices possible, and thus two types of primitive double-layer winding topology are available. This is given in gure 6.4 and 6.5 for the fundamental harmonic winding and in gure 6.6 and 6.7 for the over-harmonic winding respectively. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/9d55a31208dbe85f6368f4088b27230cfb975a2018a4fde6809647512844eaeb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/ef8a2991b901089bb05aee31db124b3b647ddab409988988ddbc11cd930e7820.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/df9b1ffbe9b2eacdf62dde3dbd476a96daddcd944178d4ce1e298abdf453e6ab.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/f50b2f15eb898951bb367018f54ef7dcb59e2e30c5f6d56a4e304b983b55d9ee.jpg)



Figure 6.4.: The rst type of normalized conductor distribution matrix and primitive double layer winding for the case of $\gamma = 1$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/d5cd6f045e76d9926a1f6444ee8e0967b60736f07d3ed97c3f47c3890b1d26c2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/05a60f3f052acffb5758e904dc5bd9a903ed62c5c4b50e164618d7d49726c1e6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/033630657de8e834457a1a150004aeccb099b7bc0448188db550a1f2e9643dce.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/c50465943fee0972b0c2ffd16793ff0b8c9ba367bfa655b66fb40f763dfe0ebb.jpg)



Figure 6.5.: The second type of normalized conductor distribution matrix and primitive double layer winding for the case of $\gamma = 1$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/ad3fe793cd1e76623c946d19a153b47513f400d66718afdc0df51c1b03b4384f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/c6a47281dde3b1310dddf71e376383848bb0b8e7a9ce58240f6d75e8f3274db6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e970b1673222ded57928f3b0b8ae2c087b923f8f6f47a6db0f22cef753b7c447.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/3dd925310c5bebcb94c0091538b1c3e7569b975a694aec2e1cb30e6194490721.jpg)



Figure 6.6.: The rst type of normalized conductor distribution matrix and primitive double layer winding for the case of $\gamma = 5$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/76ef47865f02bd72ad90e87420e198c4560fc17c1460b78f1e16a95c8fb79fdb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/dd8886d9ab1a4b4ddb785a879a5d8b30d6d26721df28d1c6328a6375dc7892ac.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/fbb3ca03f725836c2c8cbfbd2d165e4e7c0ba2e633b39af8256ba92605763969.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e7e0409f33d2bff41f1d4517eab41e4b3f732909416e7cbdf3b863b706929977.jpg)



Figure 6.7.: The second type of normalized conductor distribution matrix and primitive double layer winding for the case of $\gamma = 5$


# 6.1.1.4. The rotational symmetry and the primitive single-phase winding

After the primitive multi-phase winding is obtained, the next step is to investigate the rotational symmetry within the winding. The rotational symmetry depends on whether the topology of all the phase windings are the same or not. This is always the case for the symmetrical multiphase winding, where its name stands for. 

This is performed by applying equation 5.50 on each column vector of the normalized conductor distribution matrix. The result is a set of primitive single-phase windings with no rotational symmetry between them. 

For the investigated primitive double-layer multi-phase windings (- gure 6.4 to 6.7), there is rotational symmetry between all the phase windings, so that only one arbitrary phase winding needs to be analyzed further. 

The results are given in gure 6.8 and 6.9 for the fundamental and over-harmonic winding respectively. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/ee9d02003331ee22e15f0c996268f7e23dc73c290d5d32073eb9b9e9cc1cc561.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/6e735a832e3da9c97c600c13fa696d12d4caf3aaa1c96961ca53f368b857dad6.jpg)



(a) Winding topology of type I, left: the multi-phase winding, right: the single phase winding after considering the rotational symmetry


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/242e17013cf5817f6452d4d3083e2e0363c02fbde70d56ffde918d9f94a5bf45.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/46d7cf286e160057d3c0402f5cdd747194e68913e3ea98e5569c8e0af123d582.jpg)



(b) Winding topology of type II, left: the multi-phase winding, right: the single phase winding after considering the rotational symmetry



Figure 6.8.: The rotational symmetry and the primitive single phase winding for the case of γ = 1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/4038e77de22eab8a5216f3d0c62f40056d8c8d24f0a809cdcc52543c6dcc3574.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/7e2a04ee64e99d47879a76642ad9aa1af87cdad9d45046c43c58f6d87dda94f7.jpg)



(a) Winding topology of type I, left: the multi-phase winding, right: the single phase winding after considering the rotational symmetry


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/54b2da62ac41a9f234713d2ca4baa6462eca562fe2e4e39a487a4b0695d1c700.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e235c231274bc4e4cda6fe704d088d24d67c043ac2ec4233679f6d273e330bd5.jpg)



(b) Winding topology of type II, left: the multi-phase winding, right: the single phase winding after considering the rotational symmetry



Figure 6.9.: The rotational symmetry and the primitive single phase winding for the case of γ = 5


# 6.1.1.5. The mirror symmetry and the primitive coil group

After the primitive single-phase winding is obtained, it is to investigate whether there is further symmetrical property within it. For the most symmetrical winding, this is the case. Such symmetry is called as the mirror symmetry. 

Equation 5.53 is used to check if the mirror symmetry is within the primitive single-phase winding. If this is the case, the primitive single phase winding can be separated into two identical parts. The further discussion can be limited to one part, and the complexity of the design problem is then reduced. 

Each symmetrical part is named as primitive coil group. In general, the design purpose is to realize the primitive coil group using coils, which is generally dicult or even impossible due to given design constraints. 

The mirror symmetry, as well as the obtained primitive coil group for the fundamental and over-harmonic winding, are illustrated in gure 6.10 and 6.11 respectively, with the symmetry axis underlined with red dot line. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/067098805e304281334b476cbd1b3a7b2514fbe55db10d323769907915ad0f4f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/072cc5e6aab927ccfa47b7dc212d96d0e73ca7288a3129f2a7a06f43bb6a5aaa.jpg)



(a) Winding topology of type I, left: the primitive single phase winding, right: the primitive coil group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/b53f67d03d0cbb575472655056e8f40ae01bc5e21d94509176d43fc068363a38.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/ab84d7ee00f91c7509d528b181db334f577d2541c4ca47b4ef5c91db9eb1bdbe.jpg)



(b) Winding topology of type II, left: the primitive single phase winding, right: the primitive coil group



Figure 6.10.: The mirror symmetry and the primitive group for the case of $\gamma = 1$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/695319792d886c7e0ab5ad760318433606e1548d4de2690964c83fc97ce1b3ee.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2587e98c6729fe43ca1bcd9232e53e786b2aed225a0395b289105f6eff886bfe.jpg)



(a) Winding topology of type I, left: the primitive single phase winding, right: the primitive coil group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e482a860d653148852e10dba06ced60eb689b05c28b1d19d02ad10edc4234a5e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e810c2dabbfb8004157183c3f52517d259a520656232f5222852a0afe55101ca.jpg)



(b) Winding topology of type II, left: the primitive single phase winding, right: the primitive coil group



Figure 6.11.: The mirror symmetry and the primitive coil group for the case of $\gamma = 5$


# 6.1.1.6. The connection matrix and the primitive coils

After the primitive coil group is obtained, the next step is to connect the conductors to coils. Dierent approaches are possible, leading to winding topologies of dierent complexity and performance. 

Three types of connections are applied for each obtained primitive coil group. This results totally in 12 dierent winding topologies, which are given in gure 6.12 and 6.13: 

 the left sub-gures show the double-way connection, of which each conductor distribution is assigned to two connections and the total path of the connections is minimal over the all possible double-way connections, 

 the middle sub-gures show the single-way connection of minimal deviation, of which each conductor distribution is assigned to one connection and the total deviation between the positive and negative conductors of the connections is minimal over the all possible connections. 

 the right sub-gures show the single-way connection of shortest path, of which each conductor distribution is also assigned to one connection, and the total path of the connections is minimal over the all possible single-way connections. 

Each connection can be interpreted as a primitive coil, of which the coil pitch and position are dened. The number of turns of each primitive coil is not yet known. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e377504e1adac1ba11d3db1700d25cb082b0e5c4740af1aec6ee3887efd4a264.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/1e2e1c6adeda13cea33732f0c9df34c99893f865bd1b3aa1bb3a77f73d4dc859.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/424c55afc8d0d20748a6b7d4b7e1f18b37bf7a9ec946c7727be774423b4ef6d2.jpg)



(a) Winding topology of type I


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/72c29a94b416882c7bfa72e0e1b6a9e5ddc18a2f2bfa607281cf024fb36ba308.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/c9ad2b34129aa800b34ff88d2d9838a8e9733aaf143c389d538696d8650cad9e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/ea648e585f1f21bd1bdc0f0a2dadd9655412b4cca20de708f6d704c04b5393bb.jpg)



(b) Winding topology of type II



Figure 6. 1 2 . : The connection matrix and the primitive coils of the fundamental harmonic winding of $\gamma = 1$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/4dfda0a1ad95ba2c38734bc89df0eb552aa72d0f10e625c2d8182582e39d907b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/88829ae6bdb18b03598b1b36d1b4cdad5b4ea93e1d0a4ad5842879ff62cbaa59.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/714df50eabb12c79ce71c2798c94eaebd2217937729ab71c822611b42cba8cbb.jpg)



(a) Winding topology of type I


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/b3923a9bd006eb7d2f6a3b583de6a6160db37b02bb2e0667b6602bb5e73bca41.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/64ea2e55548a0528a03a8caf18db8702773c6e1b54973cc795737cb2d9b46956.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e3661713d5fdde94e5002913e8ef4063f41e38971e5fe19561e0953424075c69.jpg)



(b) Winding topology of type II



Figure 6. 13. : The connection matrix and the primitive coils of the over-harmonic winding of $\gamma = 5$


# 6.1.1.7. Derivation of the multi-turn and the multi-layer winding topology

The design of the multi-turn and the multi-layer winding are discussed in the same subsection, since the multi-layer winding is just a simplication of the multi-turn winding by applying equation 5.74. 

For the design of the multi-turn winding topology, the double-way connection matrix is used. An additional constraint that all of the coils have the same coil pitch is applied: 

 The double-way connections of the fundamental harmonic winding degenerates to single-way connections, as shown in the left subgures of gure 6.14a and 6.14b. It will be shown later that this is the single-way connections of the shortest path. 

 This is also the case for the over-harmonic winding of type I, which is shown in the left sub-gure of gure 6.15a. 

 A more general situation is illustrated in gure 6.15b, which is named as semi double-way connections: two conductor distributions have the double-way connection while the other two have the singleway connection. 

Applying equation 5.71 and 5.74 give the searched number of turns of each primitive coil, which is illustrated in a colored circle and is assigned to the corresponding connection (gure 6.14 and 6.15). 

as discussed above, the multi-turn and the multi-layer winding topology for the fundamental winding as well as for the over-harmonic winding ot type I are the same (as shown in gure 6.14a, 6.14b and 6.15a). A more general situation for the over-harmonic winding of type II is given in gure 6.15b. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/7ee78de6c67a193b39ae0ca44d8132bc836cd68f8b7c2724b817eb310891ca73.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/26dabb9e78743b2733ef9ed74e23d89f8755079a2d7d02c80e818d2a34cee357.jpg)



(a) Winding topology of type I


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/ded671fa967e916a662783b00551f7e1c1856de9ae34f806b5ea91ef8caee6b7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2d0d85a2586af77ce0525aac998652eeaf78614896947bd6c12aeb17fd179242.jpg)



(b) Winding topology of type II



Figure 6.14.: The multi-turn (left) and multi-layer (right) winding topology of the fundamental harmonic winding


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/bfee46088468645ecfd2145e2464f5a4ceef6aba3ac29eb383ef6948fad3710f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/8d3478a38835ffab91de3b394fba44a535635bd618fa97bb2727365e38eea8c4.jpg)



(a) Winding topology of type I


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/d9329b6bccbffb84f0385e4b75dbf94a018a0df93ceec179e472f7e5fd0c41ae.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/21121c29667229ebf8794ee46623f70a3a512d6edb1f0bc2e55e4635a42fdead.jpg)



(b) Winding topology of type II



Figure 6.15.: The multi-turn (left) and multi-layer (right) winding topology of the over-harmonic winding


# 6.1.1.8. Derivation of the multi-coil and the multi-conductor winding topology

The design of the multi-coil and the multi-conductor winding topology is discussed in the same subsection since both winding topologies are derived from the single-way connection matrix. 

For the multi-coil winding topology, the single-way connection matrix of minimal deviation is used. By applying equation 5.75, the searched number of turns of each primitive coil is obtained, which is given in gure 6.16a and 6.16b respectively. An exact reconstruction of the primitive coil groups is then possible if the primitive coils are allowed to have dierent numbers of turns. 

For the multi-conductor winding topology, the single-way connection matrix of the shortest path is used. By applying equation 5.77, 5.80, 5.79 and 5.81 successively, the searched numbers of positive conductors are obtained, which are given in gure 6.17a and 6.17b. An exact reconstruction of the primitive coil group is not possible in this case, because of the strong constraint of single conductor deviation between the positive and negative coil sides. Nevertheless, the best approximation can be obtained by applying the proposed method. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a1519c3fbd71b3b6015a479aaa8cbf7a6f2dc9aa5d0eb1f859f84ad61e13c457.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/712cb9e829a0a61d109f9bbf5e289e079665738f55f5a1d3cf1184de871ff1ca.jpg)



(a) Winding topology of type I


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/7d397479b4b34070f03b8a6ff8bac4e119aa834b57dc47ec3e381be889e21405.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/774a7f06c6c7da27c6bc0b6bdacd8a03de017ec2e5cc72c097759bd0e8ef3c1b.jpg)



(b) Winding topology of type II



Figure 6.16.: The multi-coil (left) and multi-conductor (right) winding topology of the fundamental harmonic winding


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e0fc35f99f82512af0fb8efc08d13ff8078d54cde6cd95eb72d6961ffd027199.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/cbc4d2ce5586682f29b6e3554b15175daca7a8a3745ec4a8c2d600da1b318803.jpg)



(a) Winding topology of type I


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/5a1c71c239f797c46253b992dd045071fedb727fd34683ed94246a85ba285db4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/cf485e0d1d2b441e05fc42c5361b7dc1abf1774899051bc1590c6bf4af0d873b.jpg)



(b) Winding topology of type II



Figure 6.17.: The multi-coil (left) and multi-conductor (right) winding topology of the over-harmonic winding


# 6.1.1.9. Derivation of the double-layer winding topology

The classical double-layer winding can be easily derived from the singleway connection matrix by applying equation 5.82, 5.83 and 5.84: 

 The use of the single-way connection matrix of minimal deviation generally leads to winding topologies with coils of dierent coil pitches, as shown in the left sub-gures of gure 6.18 and 6.19 for the fundamental and the over-harmonic winding topology respectively, 

 The use of the single-way connection matrix of shortest path generally leads to winding topologies with coils of the same coil pitch, as shown in the right sub-gures of gure 6.18 and 6.19 for the fundamental and the over-harmonic winding topology respectively. 

It will be shown later in this section that due to the strong constraint of the equal number of turns for all the coils, the winding factor harmonic spectrum is the same for the both derived variants. Therefore, it makes no sense to use the single-way connection matrix of minimal deviation to derive the classical double-layer winding, since the benet of the minimal deviation is eliminated by the constraint of the equal number of turns of all the coils. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/bb3313c4d2edd8cc9e80db75454664534812984a4037165dcd7ebc2fd4334741.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e93e340d32c9474f124f48e811669b6597a0cbc61abe5bad8e59c254b4c12b97.jpg)



(a) Winding topology of type I, derived from the minimal deviation connections (left) and the shortest path connections (right)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/56e2519853e95d2381ef93abdc6d9cdcc34e3bf6a430314accc69932f002c51e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/53a92bf35eb1ebc8aa23c79bb2b6b1356926fe76245a4d58745d298222e2b780.jpg)



(b) Winding topology of type II, derived from the minimal deviation connections (left) and from the shortest path connections (right)



Figure 6.18.: The classical double-layer winding topology of the fundamental harmonic winding


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/f0a7fa0fc02e2504a94f905c606d27fe0eba73b04fc6c4e8d9f12ba25a60a600.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/cd7e694352aa97ee99b86df1ced497fc9a44df2469274e5a008e5985c0fcc370.jpg)



(a) Winding topology of type I, derived from the minimal deviation connections (left) and the shortest path connections (right)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/d752810aca1b10a9a35fb8a3c1b4d2043f71d6586bdc50a0db80c5e8b5943187.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/614998e7350410749a919cca7a7fa4ae5deb56415c3685f7d9db04d5236ba71c.jpg)



(b) Winding topology of type II, derived from the minimal deviation connections (left) and from the shortest path connections (right)



Figure 6.19.: The classical double-layer winding topology of the overharmonic winding


# 6.1.1.10. Derivation of the single-layer winding topology

There is only a mirror dierence between the derivation of the doubleand the single-layer winding topology. For the derivation of the classical single-layer winding topology, the single-layer primitive coil group is used for the deviation of the single-way connection matrix. The criteria for the derivation of the single-layer primitive coil group is given in equation 5.85. 

After the connections are chosen, the classical single-layer winding topology can be obtained by applying equation 5.87 and 5.88. This is shown in gure 6.20 and 6.21 for the fundamental and over-harmonic winding respectively. 

An important conclusion can be obtained from gure 6.20 and 6.21: due to the strong constraint of single-layer topology, all the primitive winding topologies degenerate to the same winding topology. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/987e08d0875c972417a5241fa5edde8f9177285f86ac5a09b0873b06a717b1af.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a203bad553d7cec3f04ecbde8b1dd09641c21d16c1720bd57c2d388614a61fb6.jpg)



(a) Winding topology of type I, derived from the minimal deviation connections (left) and the shortest path connections (right)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/8f0523e3b8a06f1a5846376c35cf19fae5416a6a1e8c7250845ccc320f7cbe04.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a4fe3eb1cd02edb2939d838e29b3e887018e2ff2b9f61115c3b90ca0288c0aa5.jpg)



(b) Winding topology of type II, derived from the minimal deviation connections (left) and from the shortest path connections (right)



Figure 6.20.: The classical single-layer winding topology of the fundamental harmonic winding


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/f754877f56c6c1878e8a6f8995823f5a1c0ff65f17a2ce32be67a21eab668edc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/687fad9fee7e9a4274ae3f5ff718f209c37611b5882d2871565799f1f1df513c.jpg)



(a) Winding topology of type I, derived from the minimal deviation connections (left) and the shortest path connections (right)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/7f3fb630da71663031d5c23dd97ab035bc01357cd0c859901f07e9d1c7ead05e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/65e880e8fa11c2129d8dc10504f45f224ea8f3c90bb68ba4b50e1e90c8b0f7c0.jpg)



(b) Winding topology of type II, derived from the minimal deviation connections (left) and from the shortest path connections (right)



Figure 6.21.: The classical single-layer winding topology of the overharmonic winding


# 6.1.2. Evaluation and discussion of the results

# 6.1.2.1. The fundamental harmonic winding

The classical single- and double-Layer topology For the singlelayer topology of the fundamental harmonic winding, gure 6.22 gives all the possible topologies by considering the design constraints. When compared with the winding topology obtained from the star of slots method (gure 4.12), which can also be found in [63], the same winding topology is obtained by using the proposed method. 

Moreover, it is possible to show that the classical single-layer topology obtained by using the star of slots method is the optimal solution under the given constraints. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a31253f62ba561763bbb6a2da656c8ed77d00909e0d5d284614d3f752aa7aa09.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2ddc002c6e3dc38d38d1acde2411c4254b07eab9feabcf34c061f7e39a142a1f.jpg)



Figure 6.22.: The classical single-layer winding topology


For the double-layer topology of fundamental harmonic winding, - gure 6.23 shows all the possible topologies by considering the design constraints. When compared with the classical winding textbook written by H. Sequenz [63], it is clear, that the winding topology given in gure 6.23c is the well-known double-layer winding with 5/6-chording (pole pitch is equal to 6 slot pitch, and the coil pitch is equal to 5 slot pitch) which has one slot shift between the upper and lower windings. 

Moreover, the given winding topology in gure 6.23a can also be found in [63], which has the same winding factor harmonic spectrum as that of the 5/6-chording winding. Such winding is named as winding with concentric coils since the coils within the same coil group have the same center line. 

From gure 6.23, the 5/6-chording winding has a better winding factor harmonic spectrum. Therefore, it can be proved, that the wellknown 5/6-chording winding is the optimal solution under all the classical double-layer topologies. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/85979795a217f56736dee7933fabb7da5fa6641d820f22edcbfa8edc036397d2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/76e9975b78fb71018bc545d2a247bda01fbae8390a6828b2aad9e1249131c99f.jpg)



(a) Coils with dierent pitches $( \tau _ { c , 1 } = 6 , \tau _ { c , 2 } = 4 )$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/78bc9772753bbd6a749e95703f73ba8b2b0d0e060cd443c22f89f632e473950c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/19aed0c2d64af1bbe7567d257bb7eb15dc4c3b38bacd7ca3b3b7a8e19da32c2a.jpg)



(b) Coils with dierent pitches $( \tau _ { c , 1 } = 5 , \tau _ { c , 2 } = 3 )$



Figure 6.23.: The double-layer winding topology


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/67f2161998ba257a5dde808a913bc431d581acf7d2062ff836cb09445b9f26bb.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/61eb4abd741d57f8e78f6b95e74eb1c22f29e557be1e24d415a976e734dc891d.jpg)



(c) Coils with the same pitch (τc = 5)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/88722a3f4d1b07b347ac7aff6b56c27759068d39f917e9250a44d8b330096443.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/b2b890221ac18684a11133425283d156c622bfc00b683de3c1c313bf1350ee68.jpg)



(d) Coils with the same pitch $( \tau _ { c } = 4 )$



Figure 6.23.: The double-layer winding topology


The multi-turn and multi-layer topology It is interesting to notice that when the design constraints of coils with the same coil pitch is applied for the double-way connections, no multi-turn and multi-layer winding topology can be obtained. Because the double-way connection matrix degenerates to a single-way connection matrix (gure 6.14), which corresponds to the classical double-layer winding topology. According to the author's knowledge, no publications can be found for the multi-turn and multi-layer topology of the 3-phase fundamental harmonic winding with 12 slots. 

The multi-coil topology For the multi-coil topology of the fundamental harmonic winding, gure 6.24 shows all the possible winding topologies. 

A comparison with the results published by H. Schack-Nielsen in year 1940 [61], where a huge number of examples for the multi-coil topology of the fundamental harmonic winding of dierent pole-slot combinations were given, shows that for the case of 2 poles and 12 slots, the second obtained topology with the 5/6-pitch coils of 82 turns and the 3/6-pitch coils of 30 turns (gure 6.24b) is in principle the same as that H. Schack-Nielsen was found and was claimed as the best solution. 

It is to mention that in the original paper [61], these two numbers are given as 73 and 27 so that the total number of conductors of each slot is 100. As the winding topology is independent on the total number of conductors but dependent on the ratio between them, it can be simply proofed that: 

$$
7 3 \div 2 7 = 2. 7 0 \approx 8 2 \div 3 0 = 2. 7 3
$$

which is the best approximation to 2.73 under the constraint of totally 100 conductors per slot (74  26 = 2.85 and $7 2 \div 2 8 = 2 . 5 7 )$ . 

It is to mention that all the results obtained in [61] is through trying and a deterministic and systematical procedure was not mentioned. Furthermore, from the obtained winding topologies listed in gure 6.24, a better solution can be found. This is the rst obtained winding topology with the full-pitch coils of 50 turns and the 4/6-pitch coils of 58 turns (- gure 6.24a). When compared with the winding topology discussed above, the winding factor harmonic spectrum of the new winding is improved. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/1b18d3aa28d3b9e955742724e567456d2f4ec6e7534c01ac5b21b8c5c42cd25c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a0e5e7f0485dc97c4d1f33a1e74c4a15b4a5cc41beb097fea868198712a4c833.jpg)



(a) Coils with 50 and 58 turns


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/97ea5baed7d46f86a6fd6009bffa0626edffcb0e2c8f5f8c14962c2d19d23993.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/4aaf9ff4f10b08961a1569e552f29710646ff180363577f5f54027b091e1ef90.jpg)



(b) Coils with 82 and 30 turns



Figure 6.24.: The multi-coil winding topology


The multi-conductor topology For the multi-conductor topology of the fundamental harmonic winding, gure 6.25 gives all the possible topologies. 

Two possible topologies are obtained, which are derived from the singleway connection matrix of shortest path of the both types of winding topology (gure 6.16). A comparison between the both topologies shows that the rst topology is better since the deviation of the winding factor harmonic spectrum against the ideal solution is smaller. 

According to the author's knowledge, it is here the rst time to introduce such topology for the fundamental harmonic winding. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2a37b4bffdfbe688a0465d1b36274ce8532efbd20a6b81446513bfac344e1044.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a0cdea7f988fa56e0b100210545e528bbb35596411e49e5077ebad3592353481.jpg)



(a) 7 conductors of the negative coil side and 6 conductors of the positive coil side


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/230bea4489d5e95e27003d75acb677060337774d012f98fced7fd3f58fa2d696.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/183236ce42c8f434e18757fe49e3c2f7f3f74879c8535249d0a8522dbd5ab36e.jpg)



(b) 1 conductors of the negative coil side and 2 conductors of the positive coil side



Figure 6.25.: The multi-conductor winding topology


# 6.1.2.2. The over-harmonic winding

The classical double- and single-layer topology The obtained single-layer topologies derived from two dierent types of the primitive winding topologies and two dierent types of the single-way connection matrices are given in gure 6.26. Due to the strong constraints of singlelayer topology and the equal number of turns of the total coils, they degenerate to the same topology. 

When compared with the results of various publications [50, 9, 36], the same winding topology can be found, by directly applying the star of slot method. Therefore, it can be proved now that the result obtained by the star of slot method is the best solution under the given design constraints. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/0c527dbdc57dc1fd9387c67c9693fccc4bdccd9b5a5fe70d998e8250209b6a45.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2955d4c1d9426d9119b9c6dff5a0a449ba92dfc0312b4996888873ad0ea3e1fa.jpg)



Figure 6.26.: The classical single-layer winding topology


For the classical double-layer topology of the over-harmonic winding, gure 6.27 shows all the possible topologies by considering the design constraints. Four dierent topologies are obtained with totally two dierent types of winding factor harmonic spectrum. Among them, the topology given in gure 6.27b is considered as the best solution, since it is with the smallest winding factor deviation against the ideal solution and is also with the shortest coil pitches. 

When compared with the various publications [50, 9, 36], the same winding topology can be found by using the star of slots method, which is conrmed in section 4.3.1 (gure 4.13). 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2f3f456da5f4afd61195af00ac08b7fd3206354bd5f7bce8bf65f1c57c0cbc72.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/74fb0b32a6417cc7165c134be9daaf282458fa0782cf75f6448321f667325e3c.jpg)



(a) Witch concentric coils of large coil pitch


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/3e7997d5ec1db116c12317aa337acbc57c6cc6bd4121d4186c7cc8d722d15cd9.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a33a0e0f82e57ad798852620b8c98de05d52e967e3c9fb7a9e856dbaa77f95c3.jpg)



(b) With single-tooth coils



Figure 6.27.: The double-layer winding topology


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/9100d532fc6fdaf1b4bf91d8fa1e2322b38b31b8ff9ea5b10f2deec2e08ff85a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/259b0897639bbc45345290b94f14fb62311b007afa3e861255145269a1b86d0e.jpg)



(c) With concentric coils of small coil pitch


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/5488f11f728d2721fc4b27c96c6818cb75f2bed70da4e0a207e4602b58ed3bfa.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2e491a9df82ff1f139410e8bc2f734e45f5612979aedc22882de571a606c1b57.jpg)



(d) Witch single-tooth coils



Figure 6.27.: The double-layer winding topology


The multi-turn and multi-layer topology The multi-turn topology of the over-harmonic winding is given in gure 6.28. It is shown that by using two types of coils with a dierent number of turns (30 and 52), it is possible to completely cancel the sub-harmonic contents. In this case, the winding factor of the working harmonic is only slightly reduced. The same winding topology can be found in various publications [18, 42], which is obtained by modifying the classical double-layer winding 

topology. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/94586f017799790568bd1d70cfe758ddaa760c852be2312e37bdeef461d57671.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/cfe67bc59148baf60b14b803e688ef9e7cad659459ca8421baf351cac8f95cc4.jpg)



Figure 6.28.: The multi-turn winding topology


The multi-layer topology of the over-harmonic winding is given in gure 6.29. The winding has 4-layer and the number of turns of the coils is the same. Such winding topology can be also found in various publications [2, 81], where the topology is also obtained through modifying the classical double-layer winding topology. 

As the obtained multi-layer topology has exact four layers, it means that the 4-layer topology is the best solution for all the possible multilayer topologies. A further increase in the number of layers does not provide better results. 

Thus by using the proposed approach, it is not only possible to obtain such multi-layer winding topologies by a deterministic approach, but also possible to prove that the obtained number of layers is the optimal solution. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/f883692144266b86f8ca9caba38f13f7aebeecabe6b67661191e0ac0b5ffd7d7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/db0f91474424f70c3b5e8c92432e19bee51333484a067ad8b6b49ffd47654e8a.jpg)



Figure 6.29.: The multi-layer winding topology


The multi-coil topology The multi-coil topology of the over-harmonic winding is given in gure 6.30. Totally, two solutions are obtained. Both of the winding topologies have negligible small sub-harmonics contents. The winding factor harmonic spectrum of the rst topology is better because of the smaller deviation of the winding factor of the working harmonic (0.07 vs. 0.10). On the other side, the coil pitches of the second winding topology are smaller than its counterpart (coils of 1 and 3 slot pitch vs. coils of 4 and 6 slot pitch). In this case, a trade-o between the performance and the manufacturing cost should be made. 

According to the author's knowledge, such winding topology, as well as the method to obtain them, are rstly introduced by the author [11]. Such winding topology is characterized by negligible small sub-harmonic contents with a marginally more production cost. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/03e47a9560086b9548978a15cbb12ff1604e8a30eeb842eff02e5fb03f8fba58.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/b4be310cf35b2d08dea555381a0f57ab07ad2f37809050d2b72e38f7b1ff777b.jpg)



(a) Coils of 4 and 6 slot pitch


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/183a5968a8aa0f1a07791c59b9b69d2094d6b4f4853c8a7e85ac6f8e35477b7d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/10a91343861163383320942092a247d1fbe347ac5d21b3ed1f55148eff8bf916.jpg)



(b) Coils of 1 and 3 slot pitch



Figure 6.30.: The multi-coil winding topology


The multi-conductor topology For the multi-conductor topology of the over-harmonic winding, gure 6.31 shows all the possible designs. In this case, the rst winding topology gives the absolute better solution, since it is with smaller sub-harmonic contents and is with a larger winding factor of the working harmonic. 

It is interesting to notice that a similar winding topology is introduced by G. Dajaku in [20]. Instead of (6, 7), the number of conductors for the negative and positive coil sides are given as (7, 8). By using the introduced method, it can be proved that the optimal number of turns are: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a149bf51381ed57f67ec252d58b8092fd8e280c4372730961b286d5f0f718a7d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/8467e48337b25d728e4d8d32b4200c1c2cbd14ec91b66e915109c0ee2ce4f77e.jpg)



(a) 7 conductors of the positive coil side and 6 conductor of the negative coil side


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/9597c2efb7cad55cecdc3cb44920d7a1247f3d65a96f5a5f87d76d7b0b5cdc2e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a5bf435a869010d6425bad4f3532271ec369093c1750ab137ba56c7a95321be2.jpg)



(b) 2 conductors of the positive coil side and 1 conductor of the negative coil side



Figure 6.31.: The multi-conductor winding topology


$$
\left(\frac {\sqrt {3}}{2 - \sqrt {3}}, \frac {2}{2 - \sqrt {3}}\right) = (6. 4 6 4 1, 7. 4 6 4 1)
$$

As the number of turns must be an integer, the optimal results are the rounded values of (6.4641, 7.4641) towards the nearest integers, which are (6, 7). It should be noticed that 6.4641 is almost in the middle of 6 and 7. Therefore, the dierence between the two rounded values: (6, 7) and (7, 8) are so small $( 6 \div 7 - 7 \div 8 = 0 . 0 1 8 )$ ), that almost no dierence in the resulting winding factor harmonic spectrum can be observed. Nevertheless, the result proposed in [20] is not the best solution. 

After a careful analysis of this paper, two errors are found. Firstly, the proposed equation 3 in the paper is wrong: the index 1 and 2 should be interchanged. Secondly, the proposed curve in gure 4 is unfortunately not fully correct. This leads to exactly miss the best solution! A corrected curve is given in gure 6.32. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/1395263c50863a70cf1a28280d099db5243e634f7ba36de0c3bfa949a1ec7148.jpg)



(a) Original curve from [20]


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/3dff807b78ebd5fdb61a8f7aa1ed3746db18b2e4964c8bddcddf145e0b3bd984.jpg)



(b) The corrected curve



Figure 6.32.: The winding factor of the fundamental harmonic vs. the conductor ratio


# 6.2. The 3-phase winding of 9 slots with working Harmonic of 4

As a detailed example was given in the previous section, this example is used to underline some special aspects for the case of an odd number of slots. In this example, the design of a 3-phase winding with 9 slots and working harmonic of γ = 4 is considered. 

# 6.2.1. The normalized conductor distribution matrix and the primitive double layer winding

The rst and second type of the normalized conductor distribution matrix as well as the primitive double-layer winding are given in gure 6.33 and 6.34 respectively. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/9a2dc7d2be78f4789f7896ce19db3d5643ee951a75551205274138b441d81550.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e553bf62d8514ac57b288cfd549d650d9830067e8e40e929371d235d64fc4e14.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/1ce8ef4d124cac22240330d9fd028cdc67b738567c425b2e9079be7e84e27a3f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/38c57200dd466ef9899292fa09689a5144ccc128330023e4ee95f56dd8e9c110.jpg)



Figure 6.33.: The rst type of the normalized conductor distribution matrix and the primitive double layer winding


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/8300ccfe590947d3e72472006fa1d2c639778b11825bc6695cae52f1f2ac2b15.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/6e72e499affa2e48fba55c8161fe39d463792b46169abd82e65397d1b0558575.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/646dc9b820750eb766ab57b19664edf1770860b4b0e208812320b1f9386d6e4f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/8b5d8c1b69351fac43770e58f85569dae343eccd0bd21337508282d13836a6fc.jpg)



Figure 6.34.: The second type of the normalized conductor distribution matrix and the primitive double layer winding


# 6.2.2. The primitive single phase winding and the primitive coil group

The primitive single phase winding, as well as the primitive coil group, are given in gure 6.35 for the two types of primitive winding topology respectively. From the graphical representation, two important conclusions can be obtained, these are: 

 The rotational, as well as the mirror symmetry, are also available for winding topologies with an odd number of slots (gure 6.35a). 

In that case, the symmetrical order of such winding is the same as its counterpart with an even number of slots. 

However, the total number of positive conductors and the negative conductors within the primitive coil group may not be the same. This makes the reconstruction of the primitive coil group by using coils more dicult. 

 The primitive single phase winding may lack mirror symmetry (g 6.35b). In that case, the symmetrical order of such winding is lower than its counterpart with an even number of slots. It means that the primitive coil group is more complicated from the topological aspects and this leads to a more complicated winding topology. 

# 6.2.3. The double- and single-way connections

The double- and single-way connections of the investigated primitive coil groups are given in gure 6.36 for the st and second type of the winding topology respectively. 

For the case of an unequal number of positive and negative conductor distributions, it is impossible to connect all the conductor distributions using single-way connections, as illustrated in gure 6.36a. For this case, it is recommended to use the double-way connections, which leads to the multi-turn and multi-layer winding topology. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/ae931e96fc27cc30c66c54e094e1c8a8e8044ce3207207f21840723b826da674.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/11e26b09a5b6b88b7117260736c1de61921535550c6483f820e65226de862fde.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/d7ca2c7be0e6d2712a68a4a87cd0baa06c79af5002cecb503c5eeac97e3b2cdc.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/1bdff6cf4a6e781fedc64ea61705c4ea43e963fb3d618885f512018b2bb4aa1c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/7ac2e76c03477e71763873fb9ed44d58990019992bb06f2fda2261e6a682a58d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/f6acd0e9fee57a59c830b4d5e22796d1011873dfdd7af9164fcb1d5ce23934e7.jpg)



(a) Winding topology of type I



(b) Winding topology of type II



Figure 6.35.: The primitive single phase winding and the primitive coil group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/58924d9a0049010bc472170c57a49607850241e6cd3a6317f5d48c5d07f66adc.jpg)



(a) Winding topology of type I


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/451a67ab691378548b401fd7fceab4bfa529fc5afb3f917773fb39bf09a08122.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/f905824f1a7165d6a7dfb2bb419c146d936bae97e8a6b63dd09fed949f9728c4.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/c0aa804256b3d933f179cebde8b4b7bb09b3f2aafc3db37184f800d89d36d7dc.jpg)



(b) Winding topology of type II



Figure 6.36. : The double- and single-way connections : double-way connection (left) , single-way connection of minimal deviation (middle) , single-way connection of shortest path (right)


# 6.2.4. Discussion of the resulting winding topologies

The resulting winding topologies are given in gures from 6.37 to 6.42 for the multi-turn and multi-layer winding topology, the single- and doublelayer winding topology and the multi-coil and multi-conductor winding topology respectively. 

# 6.2.4.1. The multi-turn and multi-layer winding topology

There are totally two designs available for the multi-turn winding topology which are given in gure 6.37. The rst design has two dierent types of coils for the number of turns 34 and 45. The second design has three dierent types of coils for the number of turns 20, 38 and 50. Although the second design is more complicated to produce, it has the advantage that it cancels the sub-harmonic contents completely and the winding factor of the working harmonic is still quite large (ca. 0.90). 

A comparison has been made with the winding topology proposed in [18]. It leads to the conclusion that the second winding topology with winding factor of $\xi _ { 1 } = 0 . 0 0 1 3 , \xi _ { - 2 } = 0 . 0 0 0 2 , \xi _ { 4 } = 0 . 9 0 2 6$ is exactly what M.V. Cistelecan obtained through modifying the classical double-layer winding . 

A further comparison of the rst winding topology with that proposed by C. Veeh in [78] (also has two dierent types of coils) shows that the proposed winding topology has better performance (smaller sub-harmonic contents and a larger winding factor of the working harmonic). 

The corresponding multi-layer winding topology is given in gure 6.38. The second winding topology with winding factor of $\xi _ { 1 } = 0 . 0 1 0 8 , \xi _ { - 2 } =$ 0.0304, $\xi _ { 4 } = 0 . 9 0 7 2$ can be also found in the same publication by M.V. Cistelecan [18]. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/bee82aec7195f772777511f7d387495e15cd43983da841ba7e0fcb81ec1a6cf3.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/f8a8aac0e00ded5ee4bed5b023c88324cd670310f037546d3a637d3008573ad0.jpg)



(a) Coil with number of turns 45 and 34


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/c0dc114249e827fca55b97cd5d3ee6b488e6b47c3eba2b9ec2088efdaf1b3cc5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/c144375c5ed302b10991b2ffd01882bf2b52bfa4d82428d960411a0321fbc353.jpg)



(b) Coil with number of turns 20, 38 and 50



Figure 6.37.: The multi-turn winding topology


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/6eae55ffe3d8d1aad9a1ee064caedc01adc0b7fd31111b6a86ca2efc3d125327.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/08bfb1a970408e2e9ac645adf08a9d2cc1ee431f64b9050b6373287eb4579c59.jpg)



(a) Derived from gure 6.37a


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/b72505bcd4acf1587133cd5b21afb5b6de5f8c2594a3c089c16f2da96c68bfad.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/65742126a10d5edb8c371a644d3bc11555be1b6a9014f58a86e096e9f457f5ca.jpg)



(b) Derived from gure 6.37b



Figure 6.38.: The multi-layer winding topology


# 6.2.4.2. The single- and double-layer winding topology

The classical opinion is that it is not possible to construct symmetrical windings with an odd number of slots by using single-layer topology [63]. This is considered as the general drawback of such winding. It is possible to overcome the diculties by having some slots lled with more number of conductors than the other slots. An example is given in gure 6.39 where the middle slot has twice conductors than the slots on the sides. 

The obtained classical double-layer winding topology which is illustrated in gure 6.40 can be found in various publications [50, 9, 36]. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/bff7c3b64a93c6d5de8feaa72a1ee380da4641fc57226b7ba88986b690c55e8f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/66415da5eb8b05ad93650ef93efacdbac04826400c4829260cf9918cc407b804.jpg)



Figure 6.39.: The Single-layer winding topology with unique number of conductors per slot


# 6.2.4.3. The multi-coil and multi-conductor winding topology

The multi-coil topology is given in gure 6.41 with three dierent types of coils with dierent numbers of turns and dierent coil pitch. In this example, the coil with coil pitch of one slot pitch is with 88 turns, the coil with coil pitch of three slot pitch is with 58 turns, and the coil with coil pitch of six slot pitch is with 20 turns. The winding factor harmonic spectrum of this winding is with negligible small sub-harmonic contents. According to the author's knowledge, for the 3-phase winding with 9 slots and working harmonic of 4, it is for the rst time that such topology is introduced. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/6471e1dc67a838114cb0da0878f343c28f49a2ee922d6de3e263fd1045b11c66.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/f0e163f7c5d5c04adde79a2f2dd066e4aeaa12587690d834eaedef4447c144f3.jpg)



Figure 6.40.: The classical double-layer winding topology


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/188998783b371c9706366d399f6c48a912be27ec8c9dac08b2c93198747e6c99.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/9ddd94cc10aa80a9434fef8fc17d95c62870f4a81b4d098ff3e6b8c54eb7e10d.jpg)



Figure 6.41.: The multi-coil winding topology


In principle, the multi-conductor winding is more suitable for such cases, because it allows a dierent number of conductors per coil side. This solves the problem of unequal numbers of positive and negative conductor distributions within the primitive coil group. However, the obtained results given in gure 6.42 are not as expected. This is due to the very strong constraint of one conductor dierence between the positive and negative coil sides. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/001916275d7c71b63704df7cf43e68068076791deeb80b54a12f150fe28a7d2a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/4bcecbb1c5b067fa922fdf7517d383fa567d051bf4939f8a9b7ae2fbe6d17ab5.jpg)



(a) 2 conductors of the positive coil side and 3 conductors of the negative coil side


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/cf4ee52ccf53a13d5b0293e0e07c852e5ecd19a81ea42cbad43ec27e508bf927.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e6d69d11ce1fa18c629e440e483f56f3dba637d4e6d29a3c90675f31c5f0b344.jpg)



(b) 1 conductor of the positive coil side and 2 conductors of the negative coil side



Figure 6.42.: The multi-conductor winding topology


# 6.3. The 6-phase winding of 24 slots with working harmonic of 5

The last example given in this chapter is to design a 6-phase winding of 24 slots with working harmonic of 5. This example serves to show the possibility to use the proposed method to treat winding with an even number of phases. 

The normalized conductor distribution matrix and the primitive double-layer winding The normalized conductor distribution matrix and the corresponding primitive double-layer winding are given in gure 6.43 and 6.44 for the both types of primitive winding respectively. 

The primitive single phase Winding and the Primitive Coil Group After the primitive double-layer windings are obtained, by considering the rotational and mirror symmetry, the primitive single-phase windings and the primitive coil groups are obtained, which are given in gure 6.45a and 6.45b for the both types of primitive double-layer windings respectively. 

The connection matrix and the primitive coils The double- and single-way connection matrix, as well as the corresponding primitive coils, are illustrated in gure 6.46 for the both types of primitive double-layer windings respectively. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/1f5a28dad348828a51f9e917f3e6ed29bcecdbd2e4a7db4c180209da2d57906e.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/83328c557f1ce78490cda90767081b81903f018e137d161bff665f8c2f33cbc8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/38c8296eae624b247ff138b0321fb3dac7cf102b6622bbd5578baf2f65027433.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/df3171bae0cd22d24687da8d764b8dd737bf1d590f27794e8904cd16cd90c404.jpg)



Figure 6.43.: The rst type of normalized conductor distribution matrix and the primitive double layer winding


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/564388d5ad399f9aae3d824e61d2c24462722dd87b841774edb0d540e5c1d09b.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/c7e8e50ff372100d4c28a7db758772b89c3eafff4bc5deb41e956c60df4ab529.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/3f9099227cea99b011ec7a5a1b3f5dc1bb9b0d0e694c38027722a3222f88760a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/e450f0af3b5f1d5f43df644ef9e8c65c845549c82ef9131a93650c50c3620ef0.jpg)



Figure 6.44.: The second type of normalized conductor distribution matrix and the primitive double layer winding


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/2c1e22ab8db6119b0126ac40765d7bdac0c2760cafb664bf93f94034f82fb87f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a1c3b806703a5525ebb6b8b7b925be85aee123a14971332f2a6bc39fbfb002f5.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/9f0b2cdfd415ff6d4d080e1ce413ca6515928b6f9f39b6802259d620a0a747c8.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/46836c453e1fee5463d9ca07b2d9f38363227a08bfb07a8e5b8cb0bf9ff53c43.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/58f3fe9b6abd447bbaf22e328a629dddf301db7e3d3e8a31503c1e92f1d19953.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/b62e2223bbce8ecf5a5e1c29bb110f5afa525c8138fdae0789b0f94806ebe855.jpg)



(a) Winding topology of type I



(b) Winding topology of type II



Figure 6.45.: The primitive single phase winding and the primitive coil group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/a641cc96093da3e585b048d7509433914eee651d7e97527a1a4f13f953bda9bf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/04a92c83efe9e446a2151810917d9d7f8678658f20a714e8f555a0d3cc6c6497.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/f3114fd95f855a5fb41979ee222c437df7795beb4bcc25949bb674871f698472.jpg)



(a) Winding topology of type I


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/8a0cf59d7177612f8fdc13bafae10daace9706ed9a4ba01c8464f13724344cf2.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/6743d0c4e92519234d8938a0021719f824f2c1e45ac9631bfffcf2362a186cac.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/5e27db6f-e8fe-400d-8519-4727ec2f0688/4417262db7e5cb64654e88c851cd116950adb8bfa0b94a3f3e7b5420a0c74f43.jpg)



(b) Winding topology of type II


Figure 6.46. : The double- and single-way connections : double-way connection (left) , single-way connection of minimal deviation (middle) , single-way connection of shortest path (right) 

Discussion of the resulting winding topologies Two obtained winding topologies are chosen for discussion. The rst one given in gure 6.47 is the classical double-layer 6-phase winding, which is exactly that introduced by N. Domann in [24] through modifying the classical 3-phase double-layer winding. The second one given in gure 6.48 is the combination of the multi-turn and the multi-coil topologies. It is characterized by a multi-layer topology with coils of dierent numbers of turns and coil pitches. 

When compared with the classical double-layer winding (gure 6.47), where each coil group has 2 coils with coil pitch of 2 slot pitch, the novel topology introduces an additional coil with coil pitch of 7 slot pitch to surround the two coils. This leads to completely cancel the 7th overharmonic and to improve the winding factor of the working harmonic (γ = 5). 