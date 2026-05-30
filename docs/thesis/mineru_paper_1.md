![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/84849b75-b6b3-4d9a-87ae-970da05a45a1/eea80ad51a94e05a67cd335b48b2f6147f40aa7e8a22f4f8f084de0022281691.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/84849b75-b6b3-4d9a-87ae-970da05a45a1/5cc0381baa6605c53e70bb05d77d0d4255878ad1be5b7463e9ff20d02c26dfeb.jpg)



Figure 6.47.: The classical double-layer winding


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/84849b75-b6b3-4d9a-87ae-970da05a45a1/1e8b116cb6defe9d9e50ee7c8cd90587cf881291824d42d956363a91af356fec.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-05-30/84849b75-b6b3-4d9a-87ae-970da05a45a1/76c7d9c64e20e459273b1be46bbc48d770f6f0f9c22f51c55c28538c602b06ec.jpg)



Figure 6.48.: The novel multi-layer, multi-turn and multi-coil winding


# 7. Winding theory: a far from completed topic

During this research work, a unied method for the treatment of winding topologies has been achieved, which can analyze and to design all considerable winding topologies in a straightforward procedure (chapter 5 and 6). However, this does not mean that the research on this topic is completed. 

From the review of the history in this topic (chapter 3), it is learned that any innovation on the electrical machine always brings further development to this topic. As an example, the introduction of the overharmonic windings is due to the innovation of high energy permanent magnets. It was also shown in chapter 1 and 2 that the winding of the electrical machine is the key component of the electromechanical energy conversion process (chapter 1) and therefore has impacts on the overall machine performance (chapter 2). 

Based on these considerations, an outlook on the recent development in this eld is given in the last chapter of this thesis, which serves to help the academic successor to gain an overview of the recent development in this eld and so that it can better identify the ideas for the further development of this topic. 

In general, the recent development in windings of electrical machines is due to the synergy eect of integrating the electrical inverters into the winding, which makes the excitation of the windings more exible and so that more suitable for each operation point in the torque-speed plane. 

This can be categorized into two groups, which are the electric winding topology reconguration and windings with individual conductor excitation. 

# 7.1. Electric winding topology reconguration

At that time, when the electrical machine works with the 3-phase grid voltage of constant frequency and amplitude, the only possibility to change the rotor speed is to use induction motor with pole-changing windings, where the pole pairs of the winding are changed by changing the winding topology. And all this was done by electromechanical equipment. 

Since the electrical machine is fed by electrical inverters, the frequency and amplitude of the phase voltage can be varied continuously, leading to the possibility to change the rotor speed and output torque continuously. Therefore, there is no need to grasp the old technique of winding topology changing discussed above. 

However, as the electrication of the passenger vehicle becomes a major topic again, the need to recongure the winding topology is more and more clear. Without the multilevel transmission, the electrical machine should be operated both for high torque and high speed of the torquespeed plane, where the phase current and voltage are limited by the onboard battery. This problem is especially critical for electrical machines with permanent magnets excitation. 

In general, it is physically dened that for the same voltage and current limits, there are winding topologies, which can generate large torque but operate at low speed, and there are winding topologies, which can operate at high speed but generate low torque. 

Therefore, there is again investigation about winding topology reconguration, instead of electromechanical equipment, electrical inverters are used. This idea can be applied to both asynchronous machines and synchronous machines. 

# 7.1.1. Asynchronous machine

For the asynchronous machine, the purpose of the winding topology reconguration is to realize a dierent number of pole pairs. 

Miller et al. introduced a toroidally wound winding in [48], where each slot is wound with a toroidal coil. The coils are connected to a 9-phase H-Bridge inverter, making it possible to generate 4-pole and 12- pole MMF harmonics. D. Sun in [68] introduced a winding conguration, which can operate either in 9-phases with 4-poles, 3-phases with 12-poles or 3-phases with 4-poles. A comparison between the conventional winding topology, the toroidal winding topology, and the dual-rotor toroidal winding topology is also given in the same publication. The modeling (including inductance matrices, voltage, ux linkages, mechanical dynamics and torque equation) and control of the same machine (dual-vector control algorithm) during pole changing and its validation with experiment results are given by B. Ge in [29]. 

# 7.1.2. Synchronous machine

As the number of pole pairs of the synchronous machine is dened by the rotor, the purpose of the winding topology reconguration is to realize dierent connections between the phase windings, so that dierent number of turns of the phase winding can be achieved. 

Nipp in [51] investigated the so-called Switched Stator Windings with 4 dierent connections: Y-series, ∆-Series, Y-Parallel and ∆-Parallel. Swamy et al. in [70] investigated the possibility to electrically change the number of turns of the phase winding to cover a wide range of operation. Sadeghi et al. in [60] investigated dierent winding congurations for a 5-phase winding: star-, pentagon- and pentacle-connection. Atiq et al. in [5] modied the inverter operation mode to achieve ux weakening, instead of changing the winding topology. In order to expand the operating range and to have broader high eciency contour in the torque-speed plane, Hijikata et al. in [33, 34, 35] had simultaneously changed the winding topology and adapted the phase current control, which is similar to the concept of the pole-phase modulation method. 

# 7.2. Winding with individual slot excitation

The maximal exibility of the winding topology reconguration is achieved when the conductor within each slot is supplied with an individual current source. The advantages of such technique are: 

 the optimal winding factor harmonic spectrum can be achieved, as shown in chapter 5. This means, the winding factor of the working harmonic is equal to 1 and the winding factors of the sub- and over-harmonics (aside the slot harmonics) are equal to 0, 

 the maximal possibility to change the working harmonic of the ma-

chine electrically can be achieved. As shown in chapter 5, for the same set of current sources, dierent working harmonic can be realized by changing the excitation sequence of each slot conductor, 

 and the achievement of the maximal possible fault tolerance. 

All these features together with the further improvement of the fast switching power electronics (SiC and GaN) make such idea very attractive for the electrical mobility, where the power density and the fault tolerance of the electrical machine play very important roles. 

Recently more and more investigations are published in this eld [52, 30], showing the further research direction of this eld. 

In general, two concepts are considerable: massive conductors per slot with short-circuit ring as connection and toroidally wound coil per slot (Gramme-Winding). 

The idea of massive conductors per slot with short-circuit ring was rst introduced by Dajaku et al. in [21]. The advantages of such winding are summarized below: 

 the possibility to realize a very short end-winding, since one side of the massive conductors is connected by an end-connection ring, which is similar to the end-connection ring of the squirrel cage rotor. This is possible only when the sum of the Ns-phase source current is equal to 0. 

 the possibility to improve the thermal state of the stator winding by directly mounting the cooling channel on the end-ring lateral side, 

 the possibility to operate the machine for a very low DC-link voltage and to optimally use the DC-link voltage. This is because the number of conductor per phase is 1 and the conductor is directly connected to the DC-link voltage. 

An intensive analysis of this concept shows that there are some unavoidable conceptional drawbacks, which are given in [14] comprehensively: 

 the open-circuit voltage of each phase is comparable with the voltage drop over the power semiconductors of the H-bridge. This means, independent on the control strategies, the power losses within the power inverters are comparable with the mechanical power of electrical machines. Hence, the system eciency is strongly reduced and (even without the iron and rotor losses) is in the range of 

50...60%. 

 such concept is not economically feasible because rstly the current load carrying capacity of the power semiconductors lies in the range of 1000...14000 A and secondly as per slot needs 2 power semiconductors, for the case of 36 slots, there are totally 72 such IGBTs needed. 

 each massive conductor is excited with the slot leakage magnetic eld of stator frequency, which leads to extensive current losses due to skin eects. 

 although the sum of the total currents of the short-circuit ring is zero, there are locally currents with a magnitude of several kA, which cause again extensive copper losses. To reduce such copper losses, the cross section of the end-ring should be increased. 

Based on these critical points, an improved concept with toroidally wound coil per slot is introduced in the same technical report [14]. The advantages of such concept are summarized as follows: 

 By using rectangular copper conductors, a good slot lling factor can be reached. 

 It is also possible to connect all the toroidally wound coils to a shortcircuit ring. Due to the signicantly smaller current magnitude, a ring having smaller cross area can be used, without signicantly increasing the copper losses. 

 With a good design of the housing, a direct and ecient cooling of the winding is also possible. 

# 7.3. Issues of further investigation

For the research topics discussed in the previous section, there are also some issues which need further investigation: 

 The idea of using cage stator of massive conductors to increase the copper ll factor, to improve the thermal property of the winding and to simplify the production process, as Dajaku et al. proposed in [21], is generally a very interesting point. Such concept brings at the same time a major drawback, namely the eddy current eect within the massive conductor. Such eect can not be neglected anymore, especially if fast switching inverters are used. The impacts of the eddy current eect on the machine performance is a major topic if this concept is further followed, and this is till now not mentioned in the publications. 

 By the concept of toroidally wound coil per slot with individual current control, the leakage ux linkage is of the winding is increased. The impacts of the increased leakage ux linkage on the machine performance should be further investigated. Concepts of leakage ux linkage compensation are also interesting issues for further investigation. 

 The possibility to change the MMF working harmonics through changing the conductor excitation during the operation makes such concepts very attractive for machines of wide operation range. However, it is necessary to investigate the dynamic behavior of the machine during the pole-changing process and to nd out the suitable control method. 

 When the number of phases is signicantly increased, control methods without current measurement sensors or with cost-eective sensor technologies become more and more attractive. A preliminary investigation can be found in [52]. 

 When the inverters are integrated into the winding, investigations on the mechanical construction, the electromagnetic and thermal behavior of the both systems to achieve the best synergy (e.g. same cooling system for stator winding and inverters etc.) as well as on the physical interaction of the both systems should be done. 

As such issues are generally multi-physics comprehensive, this demands further development of tools for multi-physics modeling as well as methods for ecient co-simulation. 

# A. Implementation of the proposed method in Python

# A.1. Codes for the winding topology analysis

```python
def WindingSchema2WindingSpectrum(ConductorDistributionMatrix,
    MultiPhaseCurrentSystem):
    # Winding Topology
    WindingTopology = ConductorDistributionMatrix /
    np.sum(np.abs(ConductorDistributionMatrix))
    # Position Vector
    NumberOfSlots = np.size(WindingTopology, axis=0)
    PositionVector = np.linspace(0, NumberOfSlots - 1, NumberOfSlots)
    # Harmonic Vector
    if bool(NumberOfSlots % 2):  # if number of slot is even
    HarmonicNegLimit = -(NumberOfSlots + 1) / 2 + 1
    HarmonicPosLimit = (NumberOfSlots - 1) / 2
    else:
    HarmonicNegLimit = -NumberOfSlots / 2 + 1
    HarmonicPosLimit = NumberOfSlots / 2
    HarmonicVector = np.linspace(HarmonicNegLimit, HarmonicPosLimit,
    NumberOfSlots)
    # Transformation Matrix
    PositionMatrix, HarmonicMatrix = np.meshgrid(PositionVector,
    HarmonicVector)
    TransformationMatrix = np.exp(-1j * HarmonicMatrix * 2 * np.pi /
    NumberOfSlots * PositionMatrix)
    # Winding Spectrum
    WindingFactorHarmonicSpectrum =
    TransformationMatrix.dot(WindingTopology.dot(MultiPhaseCurrentSystem))
    return WindingFactorHarmonicSpectrum 
```

# A.2. Codes for the graphical presentation

# A.2.1. The winding factor harmonic spectrum

def DrawStarOfSpectrums(WindingFactorSpectrum, Color):
    # outer circle
    alpha = np.linspace(0, 2 * np.pi, 100)
    for r in np.linspace(0, 1, 6):
    plt.plot(r * np.cos(alpha), r * np.sin(alpha), linestyle=':', color='black')
    plt.plot(np.cos(alpha), np.sin(alpha), 'black')
    # harmonic vector
    NumberOfHarmonics = np.size(WindingFactorSpectrum, axis=0)
    if bool(NumberOfHarmonics % 2):
    HarmonicNegLimit = -(NumberOfHarmonics + 1) / 2 + 1
    HarmonicPosLimit = (NumberOfHarmonics - 1) / 2
    else:
    HarmonicNegLimit = -NumberOfHarmonics / 2 + 1
    HarmonicPosLimit = NumberOfHarmonics / 2
    HarmonicVector = np.linspace(HarmonicNegLimit, HarmonicPosLimit, NumberOfHarmonics)
    # dot line and harmonic order
    for i in range(0, NumberOfHarmonics):
    x = np.cos(2 * np.pi / NumberOfHarmonics * HarmonicVector[i])
    y = np.sin(2 * np.pi / NumberOfHarmonics * HarmonicVector[i])
    plt.plot([0, x], [0, y], linestyle=':', color='black')
    plt.text(1.1 * x, 1.1 * y, "%i" % HarmonicVector[i], horizontalalignment='center', verticalalignment='center')
    DrawArcArrow(Radius=1.2, ArcStart=0, ArcStop=90, Label=r' $+$ \nu\') plt.scatter(1.2, 0)
    DrawArcArrow(Radius=1.2, ArcStart=0, ArcStop=-90, Label=r' $-$ \nu\') # spectrum
    for i in range(0, NumberOfHarmonics):
    Phasor = np.abs(WindingFactorSpectrum[i]) * np.exp(1j * 2 * np.pi, color='black')
    x = np.real(Phasor)
    y = np.imag(Phasor)
    plt.plot([0, x], [0, y], Color)
    # axis configuration
    plt.axis('equal') 

```python
plt.axis('off')
plt.subplots_adjust(left=0.0, right=1., top=1., bottom=0.)
plt.show(block=False)
return 
```


A.2.2. The normalized MMF distribution


```python
def DrawStarOfMMFs(Phasors, Color, LineStyle='-', ShowArrow=False):
    Phasors = Phasors / np.amax(np.abs(Phasors))
    NumberOfPhasors = np.size(Phasors, axis=0)
    DrawPolarCoordinateSystem(np.angle(Phasors) / (2 * np.pi /
    → NumberOfPhasors))
    # ax = plt.axes()
    for i in range(0, NumberOfPhasors):
    x = (np.abs(Phasors[i]) - 0.1) * np.cos(np.angle(Phasors[i]))
    y = (np.abs(Phasors[i]) - 0.1) * np.sin(np.angle(Phasors[i]))
    plt.arrow(0, 0, x, y, head_width=0.05, head_length=0.1, fc=Color,
    → ec=Color, linestyle=LineStyle)
    if ShowArrow:
    DrawArcArrow(Radius=1.2, ArcStart=0,
    → ArcStop=180/np.pi*np.angle(Phasors[1]),
    → Label=r'\$gamma\frac{2\pi}{N_s}n'
    plt.scatter(1.2, 0)
    plt.axis('equal')
    plt.axis('off')
    plt.show(block=False)
    return 
```


A.2.3. The normalized conductor distribution matrix


```python
def DrawConnectionMatrix(
    ConnectionMatrix, MultiPhaseCurrentSystem, Color=['b', 'b', 'b'],
    WithMMF=1, WithText=[1, 1, 1], alpha=[1, 1, 1, 1, 1, 1]):
    NumberOfSlots = np.size(ConnectionMatrix, axis=0)
    ConnectionMatrix = ConnectionMatrix * NumberOfSlots
    import matplotlib
    paramstring = r'\usepackage{bm}' 
```

```prolog
matplotlib.rcParams['text.latex.preamble'] = paramstring
matplotlib.rcParams['text.usetex'] = True
NameOfPhase = [[r'\$overline {\bm{A}$', r'\$overline {\bm{B}$',
    r'\$overline {\bm{C}$',
    r'\$overline {\bm{D}$', r'\$overline {\bm{E}$',
    r'\$overline {\bm{F}$'],
    [],
    [r'\$bm{A}$', r'\$bm{B}$', r'\$bm{C}$', r'\$bm{D}$',
    r'\$bm{E}$', r'\$bm{F}$]]
for i in range(0, NumberOfSlots):
    # index
    # 1st possibility
    IndexOfPhase = np.argsort(np.abs(ConnectionMatrix[i, :]))
    IndexOfPhase = IndexOfPhase[::-1]
    SignOfPhase = np.int64(np.sign(ConnectionMatrix[i, IndexOfPhase]))
    Phasor = ConnectionMatrix[i, IndexOfPhase] *
    → MultiPhaseCurrentSystem[IndexOfPhase]
    SignOfPhase = SignOfPhase[np.nonzero(Phasor)]
    IndexOfPhase = IndexOfPhase[np.nonzero(Phasor)]
    Phasor = Phasor[np.nonzero(Phasor)]
    if Phasor.size == 0:
    continue
    x0 = (np.abs(Phasor[0]) - 0.1) * np.cos(np.angle(Phasor[0]))
    y0 = (np.abs(Phasor[0]) - 0.1) * np.sin(np.angle(Phasor[0]))
    plt.arrow(0, 0, x0, y0, head_width=0.05, head_length=0.1,
    fc=Color[IndexOfPhase[0]], ec=Color[IndexOfPhase[0]],
    → alpha=alpha[IndexOfPhase[0]])
    x0 = (np.abs(Phasor[0])) * np.cos(np.angle(Phasor[0]))
    y0 = (np.abs(Phasor[0])) * np.sin(np.angle(Phasor[0]))
    x00 = 0.2 * np.cos(np.angle(Phasor[0]))
    y00 = 0.2 * np.sin(np.angle(Phasor[0]))
    if WithoutText[IndexOfPhase[0]] == 1:
    plt.text(x0 - x00, y0 - y00,
    NameOfPhase[SignOfPhase[0] + 1][IndexOfPhase[0]],
    horizontalalignment='center',
    verticalalignment='center')
    if np.size(Phasor) == 2:
    x1 = (np.abs(Phasor[1]) - 0.1) * np.cos(np.angle(Phasor[1]))
    y1 = (np.abs(Phasor[1]) - 0.1) * np.sin(np.angle(Phasor[1]))
    plt.arrow(x0, y0, x1, y1, head_width=0.05, head_length=0.1, 
```

```python
fc=Color[IndexOfPhase[1]],
    ec=Color[IndexOfPhase[1]],
    alpha=alpha[IndexOfPhase[1]])
x1 = (np.abs(Phasor[1])) * np.cos(np.angle(Phasor[1]))
y1 = (np.abs(Phasor[1])) * np.sin(np.angle(Phasor[1]))
if WithText[IndexOfPhase[1]] == 1:
    plt.text((x0 + x1 + x0) / 2, (y0 + y1 + y0) / 2,
    NameOfPhase[SignOfPhase[1] + 1][IndexOfPhase[1]],
    horizontalalignment='center',
    verticalalignment='center')

if WithMMF:
    MmfDistribution = ConnectionMatrix.dot(MultiPhaseCurrentSystem)
    DrawStarOfMMFs(MmfDistribution, 'r', '--')
alpha = np.linspace(0, 2 * np.pi, 100)
plt.fill(0.05 * np.cos(alpha), 0.05 * np.sin(alpha), 'black')

if WithMMF == 0:
    alpha = np.linspace(0, 2 * np.pi, 100)
    plt.plot(1 * np.cos(alpha), 1 * np.sin(alpha), 'w')
plt.axis('equal')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.axis('equal')
plt.axis('off')
plt.show(block=False)
return 
```

# A.2.4. The winding topology

```python
def DrawConductorPlanOfConnectionMatrix(
    ConnectionMatrix,
    ToothWidthRatio=0.4, 0r=0.15, Color=['lime', 'gold', 'b'],
    FlagOfShow=[1, 1, 1], NumberOfConductorPerSlot=100):
    N = np.size(ConnectionMatrix, axis=0)
    ConnectionMatrix = ConnectionMatrix * N * NumberOfConductorPerSlot
    ToothOuterRadius, ToothWidth, ToothHight = DrawStator2(N,
    → ToothWidthRatio, RotationAngle=180 / N)
    for n in range(0, N):
    # position of slot
    RotationAngle = np.rad2deg(2 * np.pi / N * n) 
```

```python
# negative winding direction first
IndexOfPhase = np.argsort(ConnectionMatrix[n, :])
# find nonzero element
ConnectionVector = ConnectionMatrix[n,.IndexOfPhase]
IndexOfPhase =.IndexOfPhase[np.nonzero(ConnectionVector)]
ConnectionVector = ConnectionVector[np.nonzero(ConnectionVector)]
if ConnectionVector.size == 0:
    continue
if ConnectionVector.size == 1:
    ConnectionVector = ConnectionVector / 2
    ConnectionVector = np.append(ConnectionVector,
    → ConnectionVector)
   .IndexOfPhase = np.append(IndexOfPhase,.IndexOfPhase)
# first winding layer
Ox1 = ToothOuterRadius - Or
Oy = 0. # ToothWidth/2 + Or*2
# show phase or not
if FlagOfShow[IndexOfPhase[0]] == 1:
    if np.sign(ConnectionVector[0]) == 1:
    GoConductor(Ox1, Oy, Or, RotationAngle,
    → Color[IndexOfPhase[0]])
    elif np.sign(ConnectionVector[0]) == -1:
    ReturnConductor(Ox1, Oy, Or, RotationAngle,
    → Color[IndexOfPhase[0]])
    # text
    Tx = np.atleast_1d(Ox1) + 2.5 * Or
    Ty = np.atleast_1d(Oy) # + 0.1
    Tx, Ty = Rotation(Tx, Ty, RotationAngle)
    plt.text(Tx, Ty, "%i" % nprint(ConnectionVector[0]),
    horizontalalignment='center',
    → verticalalignment='center') # , fontsize=8)
# show phase or not
if FlagOfShow[IndexOfPhase[1]] == 1:
    # second winding layer
    Ox2 = Ox1 - 2 * Or * 1.2
    Oy = 0. # ToothWidth/2 + Or*1.4
    if np.sign(ConnectionVector[1]) == 1:
    GoConductor(Ox2, Oy, Or, RotationAngle,
    → Color[IndexOfPhase[1]])
    elif np.sign(ConnectionVector[1]) == -1:
    ReturnConductor(Ox2, Oy, Or, RotationAngle,
    → Color[IndexOfPhase[1]]) 
```

```python
Tx = np.atleast_1d(0x2) - 3. * 0r # -0.2*0r
Ty = np.atleast_1d(0y) # + 0.2
Tx, Ty = Rotation(Tx, Ty, RotationAngle)
plt.text(Tx, Ty, "%i" % np.rint(ConnectionVector[1]), horizontalalignment='center', 
    → verticalalignment='center') # , fontsize=8)
plt.axis('equal')
plt.axis('off')
plt.show(block=False)
return 
```

# A.3. Codes of the design algorithm

# A.3.1. Obtain the ideal MMF distribution from the ideal winding factor harmonic spectrum

```python
def GetMMF(WindingSpectrum_):
    # Anpassung
    MMF_ = MMF(WindingSpectrum_)
    WindingSpectrum = WindingSpectrum_.Distribution
    # Postion Vector
    NumberOfSlots = np.size(WindingSpectrum, axis=0)
    PositionVector = np.linspace(0, NumberOfSlots, NumberOfSlots,
    → endpoint=False)
    # Harmonic Order Vector
    # if number of slot is even
    if bool(NumberOfSlots % 2):
    HarmonicNegLimit = -(NumberOfSlots + 1) / 2 + 1
    HarmonicPosLimit = (NumberOfSlots - 1) / 2
    else:
    HarmonicNegLimit = -NumberOfSlots / 2 + 1
    HarmonicPosLimit = NumberOfSlots / 2
    HarmonicVector = np.linspace(HarmonicNegLimit, HarmonicPosLimit,
    → NumberOfSlots)
    # Transformation Matrix
    PositionMatrix, HarmonicMatrix = np.meshgrid(PositionVector,
    → HarmonicVector)
    TransformationMatrix = np.exp(-1j * HarmonicMatrix * 2 * np.pi /
    → NumberOfSlots * PositionMatrix) 
```

```python
# Winding Spectrum
from numpy import linalg as LA
NormalizedMMFVector = LA.solve(TransformationMatrix, WindingSpectrum)
# Anpassung
MMF_.TransformationMatrix = TransformationMatrix
MMF_.Distribution = NormalizedMMFVector
return MMF_ 
```

# A.3.2. Obtain the primitive multi-phase winding topology from the ideal MMF distribution and the multi-phase current system

```python
def GetPrimitiveMultiPhaseWinding(IdealNormalizedMMFVector_,
    SymmetricalMultiphaseCurrentSystem_):
    # Anpassung
    IdealNormalizedMMFVector = IdealNormalizedMMFVector_.Distribution
    SymmetricalMultiphaseCurrentSystem =
    SymmetricalMultiphaseCurrentSystem_.Distribution
    NumberOfMMFPhasors = np.size(IdealNormalizedMMFVector)
    NumberOfPhases = SymmetricalMultiphaseCurrentSystem_.NumberOfPhases
    # Number of Connection matrix type
    NumberOfConnectionMatrixType = 2
    # for odd and even number of slots
    if NumberOfMMFPhasors % 2:
    AngleDelta = np.exp(1j * np.pi / (2 * NumberOfMMFPhasors))
    else:
    AngleDelta = np.exp(1j * np.pi / NumberOfMMFPhasors)
    # set of connection matrix
    SetOfMultiPhaseWinding_ = []
    for h in range(0, NumberOfConnectionMatrixType):
    # connection matrix
    NormalizedConnectionMatrix = np.zeros((NumberOfMMFPhasors,
    NumberOfPhases))
    CurrentSystem_ = SymmetricalMultiphaseCurrentSystem * (AngleDelta
    ** h)
    for n in range(0, NumberOfMMFPhasors):
    MMFn = IdealNormalizedMMFVector[n]
    k0, k1 = proj(CurrentSystem_, MMFn)
    Ck0, Ck1 = CalcConnection(MMFn, CurrentSystem_, k0, k1) 
```

```txt
NormalizedConnectionMatrix[n, k0] = Ck0
NormalizedConnectionMatrix[n, k1] = Ck1
MultiPhaseWinding_ = MultiPhaseWinding(IdealNormalizedMMFVector_, CurrentSystem_)
NormalizedConnectionMatrix[np.abs(NormalizedConnectionMatrix) < 1E-6] = 0
MultiPhaseWinding_.ConnectionMatrix = NormalizedConnectionMatrix
SetOfMultiPhaseWinding_.append(MultiPhaseWinding_)
return SetOfMultiPhaseWinding_ 
```

# A.3.3. Obtain the primitive single-phase winding topology through detecting the rotation symmetry

```python
def GetSinglePhaseWinding(SetOfConnectionMatrix, CurrentSystemFlag):
    NumberOfConnectionMatrixType = len(SetOfConnectionMatrix)
    SetOfSinglePhaseWinding = []
    for n in range(0, NumberOfConnectionMatrixType):
    ConnectionMatrix = SetOfConnectionMatrix[n].ConnectionMatrix
    FlagOfSymmetry = 0
    N = np.size(ConnectionMatrix, axis=0)
    m = np.size(ConnectionMatrix, axis=1)
    n1 = np.linspace(0, N, N, endpoint=False, dtype=np.int)
    n2 = np.linspace(0, m, m, endpoint=False, dtype=np.int)
    for g in range(1, N):
    # break from the outer loop
    if FlagOfSymmetry == 1:
    break
    for h in range(1, m):
    k1 = np.mod(n1 + g, N)
    k2 = np.mod(n2 + h, m)
    MatrixOfRotationSymmetryTypeI = np.zeros((N, N))
    MatrixOfRotationSymmetryTypeII = np.zeros((m, m))
    MatrixOfRotationSymmetryTypeI[n1, k1] = 1
    MatrixOfRotationSymmetryTypeII[n2, k2] = 1
    # Residum
    ConnectionMatrix_ = ConnectionMatrix.copy()
    if CurrentSystemFlag == 1:
    # the topology of the last phase and the first phase
    → are the same, except for the sign!
    ConnectionMatrix_[:, 0] = -ConnectionMatrix_[:, 0] 
```

```python
Residum = ConnectionMatrix_ -
    → MatrixOfRotationSymmetryTypeI.dot(ConnectionMatrix).dot(
    MatrixOfRotationSymmetryTypeII)
# break from the inner loop
if LA.norm(Residum, np.inf) < 1E-10:
    FlagOfSymmetry = 1
    MatrixOfRotationSymmetry =
    → MatrixOfRotationSymmetryTypeI
    MatrixOfRotationSymmetryTypeII =
    → MatrixOfRotationSymmetryTypeII
    ConnectionVector = ConnectionMatrix[:, 0]
    break
else:
    MatrixOfRotationSymmetry = np.zeros((N, N))
    MatrixOfRotationSymmetryTypeII = np.zeros((N, N))
    ConnectionVector = np.zeros(N)
SinglePhaseWinding_ = SinglePhaseWinding(SetOfConnectionMatrix[n])
SinglePhaseWinding_.ConnectionVector = ConnectionVector
SinglePhaseWinding_.RoationSymmetryMatrix =
    → MatrixOfRotationSymmetry
SinglePhaseWinding_.RoationSymmetryMatrixTypeII =
    → MatrixOfRotationSymmetryTypeII
SinglePhaseWinding_.FlagOfSymmetry = FlagOfSymmetry
SetOfSinglePhaseWinding.append(SinglePhaseWinding_)
return SetOfSinglePhaseWinding 
```

# A.3.4. Obtain the primitive coil group through detecting the mirror symmetry

```python
def GetCoilGroup(SetOfPhaseWinding):
    NumberOfConnectionMatrixType = len(SetOfPhaseWinding)
    SetOfCoilGroup = []
    for n in range(0, NumberOfConnectionMatrixType):
    ConnectionVector = SetOfPhaseWinding[n].ConnectionVector
    FlagOfMirrorSymmetry, MatrixOfMirrorSymmetry,
    → PositionOfSymmetryAxis =
    → DetectMirrorSymmetry(ConnectionVector)
    if FlagOfMirrorSymmetry == 1:
    UpperPartOfConnectionVector, _MatrixOfMirrorSymmetry = \
    GetPartOfMirrorSymmetry(MatrixOfMirrorSymmetry, 
```

```python
PositionOfSymmetryAxis,
    ConnectionVector, 'U')
else: # in case of no mirror symmetry
    UpperPartOfConnectionVector = ConnectionVector
    MatrixOfMirrorSymmetry = _MatrixOfMirrorSymmetry =
    np.identity(np.size(ConnectionVector))
CoilGroup_ = CoilGroup(SetOfPhaseWinding[n])
CoilGroup_.ConnectionVector = UpperPartOfConnectionVector
CoilGroup_.FlagOfSymmetry = FlagOfMirrorSymmetry
CoilGroup_.MirrorSymmetryMatrix = _MatrixOfMirrorSymmetry
CoilGroup_.MirrorSymmetryMatrix = MatrixOfMirrorSymmetry
CoilGroup_.PositionOfSymmetricAxis = PositionOfSymmetryAxis
SetOfCoilGroup.append(CoilGroup_)
return SetOfCoilGroup 
```

# A.3.5. Obtain the primitive coils through detecting the connection matrix

```python
def WindingTopologyDoubleWayConnection(SetOfCoilGroup5):
    SetOfPriMultiLayerTurnPitchTop = []

    for i in range(len(SetOfCoilGroup5)):
    # %%
    a = SetOfCoilGroup5[i]
    WorkingHarmonic =
    → a.ParentSinglePhaseWinding.ParentMultiPhaseWinding. \
    ParentMMF.ParentWindingSpectrum.WorkingHarmonic
    MSymMatrix = a.MirrorSymmetryMatrix
    RSymMatrixI = a.ParentSinglePhaseWinding.RoationSymmetryMatrix
    RSymMatrixII =
    → a.ParentSinglePhaseWinding.RoationSymmetryMatrixTypeII
    MPhaCurrSys =
    → a.ParentSinglePhaseWinding.ParentMultiPhaseWinding.CurrentSystem
    _MSymMatrix = a._MirrorSymmetryMatrix
    ConductorDistributionIdeal = a.ConnectionVector
    ConductorDistributionIdeal = nprint(ConductorDistributionIdeal *
    → ConductorDistributionIdeal.size * 1e2).astype(
    int)
    # %% Double-Way Connection: Approximation using multi-layer
    → topology (4-layer)
    _ConductorDistributionIdeal = ConductorDistributionIdeal 
```

_ConnectionVector, _CoilPitchVector, _NumberOfCoils = $\Leftrightarrow$ ObtainSetOfConnection(_ConductorDistributionIdeal)
    _ConnectionMatrix = np.zeros(_ConductorDistributionIdeal.size, $\Leftrightarrow$ _NumberOfCoils))
for i in range(_NumberOfCoils):
    _ConnectionMatrix[_ConnectionVector[i, 0], i] = 1
    _ConnectionMatrix[_ConnectionVector[i, 1], i] = -1
    _NumberOfTurns, _ErrorRel, _ConductorDistributionReal = \
    CalculateNumberOfTurns(_ConnectionMatrix,
    _ConductorDistributionIdeal)
    PriMultiLayerTurnPitchTopo1 = PriMultiLayerTurnPitchTopo(
    _ConductorDistributionIdeal,
    _ConductorDistributionReal,
    _ConnectionVector, _CoilPitchVector, _ConnectionMatrix,
    _NumberOfTurns, _ErrorRel,
    MSymMatrix=MSymMatrix, RSymMatrixI=RSymMatrixI,
    RSymMatrixII=RSymMatrixII, MPhaCurrSys=MPhaCurrSys,
    _MSymMatrix=_MSymMatrix,
    WorkingHarmonic=WorkingHarmonic)
    SetOfPriMultiLayerTurnPitchTop.append(PriMultiLayerTurnPitchTopo1)
return SetOfPriMultiLayerTurnPitchTop

def WindingTopologySingleWayConnectionMD(SetOfCoilGroup5):
    SetOfPriDLayerMTurnMPitchTopo = []
    for i in range(len(SetOfCoilGroup5)):
    # %#
    a = SetOfCoilGroup5[i]
    WorkingHarmonic = $\Leftrightarrow$ a.ParentSinglePhaseWinding.ParentMultiPhaseWinding.\
    ParentMMF.ParentWindingSpectrum.WorkingHarmonic
    MSymMatrix = a.MirrorSymmetryMatrix
    _MSymMatrix = a._MirrorSymmetryMatrix
    RSymMatrixI = a.ParentSinglePhaseWinding.RoationSymmetryMatrix
    RSymMatrixII = $\Leftrightarrow$ a.ParentSinglePhaseWinding.RoationSymmetryMatrixTypeII
    MPhaCurrSys = $\Leftrightarrow$ a.ParentSinglePhaseWinding.ParentMultiPhaseWinding.CurrentSystem
    ConductorDistributionIdeal = a.ConnectionVector
    ConductorDistributionIdeal = np.rint(ConductorDistributionIdeal * $\Leftrightarrow$ ConductorDistributionIdeal.size * 1e2).astype(
    int) 

```python
# % Single-Way Connection: Multi-Coil Approach
_ConductorDistributionIdeal = ConductorDistributionIdeal
_ConnectionVector, _CoilPitchVector, _NumberOfCoils =
ObtainMCoilConnection(_ConductorDistributionIdeal)
_ConnectionMatrix = np.zeros(_ConductorDistributionIdeal.size,
NumberOfCoils))
for i in range(_NumberOfCoils):
    _ConnectionMatrix[_ConnectionVector[i, 0], i] = 1
    _ConnectionMatrix[_ConnectionVector[i, 1], i] = -1
_NumberOfTurns, _ErrorRel, _ConductorDistributionReal = \
CalculateNumberOfTurns(_ConnectionMatrix,
_ConductorDistributionIdeal)
PriDLayerMTurnMPitchTopo = PriMultiLayerTurnPitchTopo(
_ConductorDistributionIdeal, _ConductorDistributionReal,
_ConnectionVector, _CoilPitchVector, _ConnectionMatrix,
_NumberOfTurns, _ErrorRel,
MSymMatrix=MSymMatrix, RSymMatrixI=RSymMatrixI,
RSymMatrixII=RSymMatrixII, MPhaCurrSys=MPhaCurrSys,
_MSymMatrix=_MSymMatrix, WorkingHarmonic=WorkingHarmonic)
SetOfPriDLayerMTurnMPitchTopo.append(PriDLayerMTurnMPitchTopo)
return SetOfPriDLayerMTurnMPitchTopo

def WindingTopologySingleWayConnectionSP(SetOfCoilGroup5):
    SetOfPriDLayerMCondMPitchTopo = []
    for i in range(len(SetOfCoilGroup5)):
    # %#
    a = SetOfCoilGroup5[i]
    WorkingHarmonic =
    a.ParentSinglePhaseWinding.ParentMultiPhaseWinding. \
    ParentMMF.ParentWindingSpectrum.WorkingHarmonic
MSymMatrix = a.MirrorSymmetryMatrix
_MSymMatrix = a._MirrorSymmetryMatrix
RSymMatrixI = a.ParentSinglePhaseWinding.RoationSymmetryMatrix
RSymMatrixII =
    a.ParentSinglePhaseWinding.RoationSymmetryMatrixTypeII
MPhaCurrSys =
    a.ParentSinglePhaseWinding.ParentMultiPhaseWinding.CurrentSystem
ConductorDistributionIdeal = a.ConnectionVector
ConductorDistributionIdeal = nprint(ConductorDistributionIdeal *
ConductorDistributionIdeal.size * 1e2).astype(
int) 
```

```python
# % Single-Way Connection: Multi-Conductor
_ConductorDistributionIdeal = ConductorDistributionIdeal
_ConnectionVector, _CoilPitchVector, _NumberOfCoils =
ObtainMCondConnection(_ConductorDistributionIdeal)
_ConnectionMatrix = np.zeros(_ConductorDistributionIdeal.size,
_NumberOfCoils + 1))
MultiCondMatrix = np.zeros(_ConductorDistributionIdeal.size,
_NumberOfCoils))
for i in range(_NumberOfCoils):
    _ConnectionMatrix[_ConnectionVector[i, 0], i] = +1
    _ConnectionMatrix[_ConnectionVector[i, 1], i] = -1
    # one more column for additional conductor
    _ConnectionMatrix[_ConnectionVector[i, 1], -1] = np.sign( np.sum(_ConductorDistributionIdeal[_ConnectionVector[i,
    :])]
    # save the additional conductor in a extra matrix
    MultiCondMatrix[_ConnectionVector[i, 1], i] = np.sign( np.sum(_ConductorDistributionIdeal[_ConnectionVector[i,
    :])]
    _NumberOfTurns, _ErrorRel, _ConductorDistributionReal = \
    CalculateNumberOfTurns(_ConnectionMatrix,
    _ConductorDistributionIdeal)
# normalization
if _NumberOfTurns[-1] == 0:
    _NumberOfTurns = _NumberOfTurns
else:
    _NumberOfTurns = _NumberOfTurns / _NumberOfTurns[-1]
# number of conductor should be integer: round-off
_NumberOfTurns = np.rint(_NumberOfTurns)
_ConductorDistributionReal = _ConnectionMatrix.dot(_NumberOfTurns)
ConnectionMatrix = _ConnectionMatrix[:, :-1]
NumberOfTurns = _NumberOfTurns[:-1]
_ErrorAbs = _ConductorDistributionReal * _NumberOfTurns[-1] -
→ _ConductorDistributionIdeal
_ErrorRel = LA.norm(_ErrorAbs.astype(float)) /
→ LA.norm(_ConductorDistributionIdeal.astype(float))
PriDLayerMCondMPitchTopo = PriMultiLayerTurnPitchTopo(
    _ConductorDistributionIdeal, _ConductorDistributionReal,
    _ConnectionVector, _CoilPitchVector, ConnectionMatrix,
    NumberOfTurns, _ErrorRel, MultiCondMatrix=MultiCondMatrix,
    MSymMatrix=MSymMatrix, RSymMatrixI=RSymMatrixI,
    RSymMatrixII=RSymMatrixII, MPhaCurrSys=MPhaCurrSys, 
```

```txt
_MSymMatrix=_MSymMatrix, WorkingHarmonic=WorkingHarmonic)
SetOfPriDLayerMCondMPitchTopo.append(PriDLayerMCondMPitchTopo)
return SetOfPriDLayerMCondMPitchTopo 
```


A.3.6. Obtain the coils of particular winding topology


```python
def ObtainMultiTurnWindingTopology(SetOfPriMultiLayerTurnPitchTopo5):
    SetOfPriMLayerMTurnSPitchTopo = []
    for i in range(len(SetOfPriMultiLayerTurnPitchTopo5)):
    PriMultiLayerTurnPitchTopo1 = SetOfPriMultiLayerTurnPitchTopo5[i]
    # who remains: remove the unequal coil pitch
    _CoilPitch = PriMultiLayerTurnPitchTopo1.CoilPitch
    UniqueCoilPitch, InverseIndex, NumberOfCoils =
    → np.unique(_CoilPitch, return_counts=True,
    → return_inverse=True)
    _IndexOfMaxNumberOfCoils = np.argmax(NumberOfCoils)
    _CoilPitchOfMaxNumberOfCoils =
    → UniqueCoilPitch[_IndexOfMaxNumberOfCoils]
    _IndexOfCoils = np.where(_CoilPitch ==
    → _CoilPitchOfMaxNumberOfCoils)[0]
    _CoilPitch = PriMultiLayerTurnPitchTopo1.CoilPitch[_IndexOfCoils]
    _ConnectionMatrix =
    → PriMultiLayerTurnPitchTopo1.ConnectionMatrix[:,
    → _IndexOfCoils]
    _ConnectionVector =
    → PriMultiLayerTurnPitchTopo1.ConnectionVector[_IndexOfCoils,
    → :]
    _ConductorDistributionIdeal =
    → PriMultiLayerTurnPitchTopo1.ConductorDistributionIdeal
# solve the equation system
    _NumberOfTurns, _ErrorRel, _ConductorDistributionReal = \
    CalculateNumberOfTurns(_ConnectionMatrix,
    _ConductorDistributionIdeal)
    PriMLayerMTurnSPitchTopo = PriMultiLayerTurnPitchTopo(
    _ConductorDistributionIdeal, _ConductorDistributionReal,
    _ConnectionVector, _CoilPitch, _ConnectionMatrix,
    _NumberOfTurns, _ErrorRel,
    MSymMatrix=PriMultiLayerTurnPitchTopo1.MSymMatrix,
    RSymMatrixI=PriMultiLayerTurnPitchTopo1.RSymMatrixI,
    RSymMatrixII=PriMultiLayerTurnPitchTopo1.RSymMatrixII, 
```

```python
MPhaCurrSys=PriMultiLayerTurnPitchTopo1.MPhaCurrSys,
_MSymMatrix=PriMultiLayerTurnPitchTopo1._MSymMatrix,
WorkingHarmonic=PriMultiLayerTurnPitchTopo1.WorkingHarmonic)
SetOfPriMLayerMTurnSPitchTopo.append(PriMLayerMTurnSPitchTopo)
return SetOfPriMLayerMTurnSPitchTopo

def ObtainMultiLayerWindingTopology(SetOfPriMLayerMTurnSPitchTopo):
    SetOfPriMLayerSTurnTopo = []
    for i in range(len(SetOfPriMLayerMTurnSPitchTopo)):
    PriMLayerMTurnSPitchTopo = SetOfPriMLayerMTurnSPitchTopo[i]
    _NumberOfTurns = PriMLayerMTurnSPitchTopo.NumberOfTurns
    _NumberOfTurns = np.rint(_NumberOfTurns / np.amin(_NumberOfTurns))
    → * np.amin(_NumberOfTurns)
    _ConnectionMatrix = PriMLayerMTurnSPitchTopo.ConnectionMatrix
    _ConnectionVector = PriMLayerMTurnSPitchTopo.ConnectionVector
    _CoilPitch = PriMLayerMTurnSPitchTopo.CoilPitch
    _ConductorDistributionReal = _ConnectionMatrix.dot(_NumberOfTurns)
    _ConductorDistributionIdeal =
    → PriMLayerMTurnSPitchTopo.ConductorDistributionIdeal
    _ErrorAbs = _ConductorDistributionReal -
    → _ConductorDistributionIdeal
    _ErrorRel = LA.norm(_ErrorAbs.astype(float)) /
    → LA.norm(_ConductorDistributionIdeal.astype(float))
    PriMLayerSTurnTopo = PriMultiLayerTurnPitchTopo(
    _ConductorDistributionIdeal, _ConductorDistributionReal,
    _ConnectionVector, _CoilPitch, _ConnectionMatrix,
    _NumberOfTurns, _ErrorRel,
    MSymMatrix=PriMLayerMTurnSPitchTopo.MSymMatrix,
    RSymMatrixI=PriMLayerMTurnSPitchTopo.RSymMatrixI,
    RSymMatrixII=PriMLayerMTurnSPitchTopo.RSymMatrixII,
    MPhaCurrSys=PriMLayerMTurnSPitchTopo.MPhaCurrSys,
    _MSymMatrix=PriMLayerMTurnSPitchTopo._MSymMatrix,
    WorkingHarmonic=PriMLayerMTurnSPitchTopo.WorkingHarmonic)
    SetOfPriMLayerSTurnTopo.append(PriMLayerSTurnTopo)
    return SetOfPriMLayerSTurnTopo 
```

```txt
# %% double- and single-layer single turn: can be obtained from multi-coil
→ or multi-conductor 
```

```python
def ObtainDoubleLayerWindingTopology2(SetOfPriDLayerMTurnMPitchTopo5):
    # start from single pitch, since solution of multi pitch with negative
    SetOfPriDLayerSTurnTopo = []
    for i in range(len(SetOfPriDLayerMTurnMPitchTopo5)): 
```

```txt
PriMultiLayerTurnPitchTopo1 = SetOfPriDLayerMTurnMPitchTopo5[i]
# calculate
_CoilPitch = PriMultiLayerTurnPitchTopo1.CoilPitch
# actual connection matrix
ConnectionMatrix =
    np.sign(PriMultiLayerTurnPitchTopo1.ConnectionMatrix)
# for calculation
_ConnectionMatrix = np.sum(ConnectionMatrix, axis=1)
_ConnectionVector = PriMultiLayerTurnPitchTopo1.ConnectionVector
_ConductorDistributionIdeal =
    PriMultiLayerTurnPitchTopo1.ConductorDistributionIdeal
_NumberOfTurns, _ErrorRel, _ConductorDistributionReal =
    CalculateNumberOfTurns(
    np.atleast_2d(_ConnectionMatrix).transpose(),
    _ConductorDistributionIdeal)
NumberOfTurns = _NumberOfTurns * np.ones(_CoilPitch.size)
# save results
PriDLayerSTurnTopo = PriMultiLayerTurnPitchTopo(
    _ConductorDistributionIdeal, _ConductorDistributionReal,
    _ConnectionVector, _CoilPitch, ConnectionMatrix,
    NumberOfTurns, _ErrorRel,
    MSymMatrix=PriMultiLayerTurnPitchTopo1.MSymMatrix,
    RSymMatrixI=PriMultiLayerTurnPitchTopo1.RSymMatrixI,
    RSymMatrixII=PriMultiLayerTurnPitchTopo1.RSymMatrixII,
    MPhaCurrSys=PriMultiLayerTurnPitchTopo1.MPhaCurrSys,
    _MSymMatrix=PriMultiLayerTurnPitchTopo1._MSymMatrix,
    WorkingHarmonic=PriMultiLayerTurnPitchTopo1.WorkingHarmonic)
SetOfPriDLayerSTurnTopo.append(PriDLayerSTurnTopo)
return SetOfPriDLayerSTurnTopo 
```

# Bibliography



[1] H. Akita et al. New core structure and manufacturing method for high eciency of permanent magnet motors. In: 38th IAS Annual Meeting on Conference Record of the Industry Applications Conference, 2003. Vol. 1. 2003, 367372 vol.1. doi: 10.1109/IAS.2003. 1257527. 





[2] L. Alberti and N. Bianchi. Theory and Design of Fractional-Slot Multilayer Windings. In: IEEE Transactions on Industry Applications 49.2 (2013), pp. 841849. issn: 0093-9994. doi: 10.1109/ TIA.2013.2242031. 





[3] K. Atallah and D. Howe. A novel high-performance magnetic gear. In: IEEE Transactions on Magnetics 37.4 (2001), pp. 28442846. issn: 0018-9464. doi: 10.1109/20.951324. 





[4] K. Atallah et al. Design and Operation of a Magnetic Continuously Variable Transmission. In: IEEE Transactions on Industry Applications 48.4 (2012), pp. 12881295. issn: 0093-9994. doi: 10. 1109/TIA.2012.2199451. 





[5] S. Atiq, T. A. Lipo, and B. i. Kwon. Novel eld weakening technique for Surface Mounted Permanent Magnet machine using Current Regulated Voltage Source Inverters. In: 2014 International Symposium on Power Electronics, Electrical Drives, Automation and Motion. 2014, pp. 836841. doi: 10.1109/SPEEDAM.2014.6871964. 





[6] V. Bedjanic. Beitrag zur Theorie der zweischichtigen symmetrischen Bruchlochwicklungen. In: Elektrotechnik und Maschinenbau 59 (1941), p. 499. 





[7] N. Bekka et al. A Novel Methodology for Optimal Design of Fractional Slot With Concentrated Windings. In: IEEE Transactions on Energy Conversion 31.3 (2016), pp. 11531160. issn: 0885-8969. doi: 10.1109/TEC.2016.2552546. 





[8] N. Bekka et al. Optimization of the MMF function of fractional slot concentrated windings. In: 2014 International Conference on Electrical Machines (ICEM). 2014, pp. 616622. doi: 10 . 1109 / ICELMACH.2014.6960244. 





[9] N. Bianchi and M. Dai Pre. Use of the star of slots in designing fractional-slot single-layer synchronous motors. In: vol. 153. 3. 2006, pp. 459466. doi: 10.1049/ip-epa:20050284. 





[10] D. H. Braymer and A. C. Roe. Repair-shop diagrams and connecting tables for lap-wound induction motors: practical step-by-atep information and instructions for connecting all types of windings for two-phase and three-phase motors of 2 to 24 poles. McGraw-Hill, 1946. 416 pp. 





[11] M. Cai, M. Henke, and W. R. Canders. An improved method for design of symmetrical multiphase winding with optimal space harmonics spectrum. In: 2014 17th International Conference on Electrical Machines and Systems (ICEMS). 2014, pp. 34693475. doi: 10.1109/ICEMS.2014.7014090. 





[12] W.-R. Canders and D. Hülsmann. Analysis and classication of bearingless machines with symmetric 3-phase concentrated windings. In: The XIX International Conference on Electrical Machines - ICEM 2010. 2010, pp. 16. doi: 10.1109/ICELMACH.2010. 5607764. 





[13] W.-R. Canders and D. Hülsmann. Analysis and Determination of Symmetrical Three-Phase Windings with Focus on Tooth Coil Windings. In: XV International Symposium on Electromagnetic Fields in Mechatronics, Electrical and Electronic Engineering, ISEF 2011. 2011. 





[14] W.-R. Canders and H. Mosebach. Multiphase Machine with Individual Slot Control. German. Tech. rep. Institute for Electrical Machines, Traction and Drives, TU Braunschweig, 2016. 





[15] R. Cipin and M. Patocka. Electromagnetic design of irregular three phase windings. In: 2013 15th European Conference on Power Electronics and Applications (EPE). 2013, pp. 110. doi: 10.1109/EPE. 2013.6631824. 





[16] R. Cipín and M. Pato£ka. New innitesimal method for the analysis and synthesis of AC machines winding. In: International Aegean Conference on Electrical Machines and Power Electronics and Electromotion, Joint Conference. 2011, pp. 693698. doi: 10.1109/ ACEMP.2011.6490684. 





[17] M. V. Cistelecan, F. J. T. E. Ferreira, and M. Popescu. Three phase tooth-concentrated interspersed windings with low space harmonic content. In: The XIX International Conference on Electrical Machines - ICEM 2010. 2010, pp. 16. doi: 10.1109/ICELMACH. 2010.5608144. 





[18] M. V. Cistelecan, F. J. T. E. Ferreira, and M. Popescu. Three phase tooth-concentrated multiple-layer fractional windings with low space harmonic content. In: 2010 IEEE Energy Conversion Congress and Exposition. 2010, pp. 13991405. doi: 10 . 1109 / ECCE.2010.5618267. 





[19] G. Dajaku and D. Gerling. A Novel 24-Slots/10-Poles Winding Topology for Electric Machines. In: 2011 IEEE International Electric Machines Drives Conference (IEMDC). 2011, pp. 6570. doi: 10.1109/IEMDC.2011.5994889. 





[20] G. Dajaku and D. Gerling. Eddy current loss minimization in rotor magnets of PM machines using high-eciency 12-teeth/10-slots winding topology. In: 2011 International Conference on Electrical Machines and Systems. 2011, pp. 16. doi: 10.1109/ICEMS.2011. 6073360. 





[21] G. Dajaku and D. Gerling. Low costs and high eciency asynchronous machine with stator cage winding. In: 2014 IEEE International Electric Vehicle Conference (IEVC). 2014, pp. 16. doi: 10.1109/IEVC.2014.7056083. 





[22] G. Dajaku et al. Comparison of Two Dierent IPM Traction Machines With Concentrated Winding. In: IEEE Transactions on Industrial Electronics 63.7 (2016), pp. 41374149. issn: 0278-0046. doi: 10.1109/TIE.2016.2544720. 





[23] A. Di Gerlando, R. Perini, and M. Ubaldini. High pole number, PM synchronous motor with concentrated coil armature windings. In: Recent Developments of Electrical Drives: Best papers from the International Conference on Electrical Machines ICEM'04. Springer Netherlands, 2006, pp. 307320. isbn: 978-1-4020-4535-6. doi: 10.1007/978-1-4020-4535-6_26. 





[24] N. Domann and M. Henke. Design and build-up of a high performance six-phase machine for an automotive application. In: 2014 International Conference on Electrical Machines (ICEM). 2014, pp. 20802086. doi: 10.1109/ICELMACH.2014.6960471. 





[25] A. El-Refaie. Fractional-slot concentrated-windings: A paradigm shift in electrical machines. In: 2013 IEEE Workshop on Electrical Machines Design, Control and Diagnosis (WEMDCD). 2013, pp. 2432. doi: 10.1109/WEMDCD.2013.6525162. 





[26] A. M. EL-Refaie. Fractional-Slot Concentrated-Windings Synchronous Permanent Magnet Machines: Opportunities and Challenges. In: IEEE Transactions on Industrial Electronics 57.1 (2010), pp. 107 121. issn: 0278-0046. doi: 10.1109/TIE.2009.2030211. 





[27] A. M. El-Refaie and M. R. Shah. Comparison of Induction Machine Performance with Distributed and Fractional-Slot Concentrated Windings. In: 2008 IEEE Industry Applications Society Annual Meeting. 2008, pp. 18. doi: 10.1109/08IAS.2008.30. 





[28] E. Fornasiero, N. Bianchi, and S. Bolognani. Slot Harmonic Impact on Rotor Losses in Fractional-Slot Permanent-Magnet Machines. In: IEEE Transactions on Industrial Electronics 59.6 (2012), pp. 25572564. issn: 0278-0046. doi: 10.1109/TIE.2011.2168794. 





[29] B. Ge et al. Winding Design, Modeling, and Control for Pole-Phase Modulation Induction Motors. In: IEEE Transactions on Magnetics 49.2 (2013), pp. 898911. issn: 0018-9464. doi: 10.1109/ TMAG.2012.2208652. 





[30] D. Gerling et al. Analytical calculation of the novel Stator Cage Machine. In: 2015 18th International Conference on Electrical Machines and Systems (ICEMS). 2015, pp. 13461352. doi: 10.1109/ ICEMS.2015.7385248. 





[31] J. J. Germishuizen and M. J. Kamper. Classication of symmetrical non-overlapping three-phase windings. In: The XIX International Conference on Electrical Machines - ICEM 2010. 2010, pp. 16. doi: 10.1109/ICELMACH.2010.5608096. 





[32] H. Hatano. Development of High Thermal Conducting Insulation for Turbine Generator Stator Coil. Tech. rep. Power and Industrial System R&D Center, TOSHIBA Corporation. 





[33] H. Hijikata et al. MATRIX motor with individual winding current control capability for variable parameters and iron loss suppression. In: 2014 International Conference on Electrical Machines (ICEM). 2014, pp. 551557. doi: 10.1109/ICELMACH.2014. 6960234. 





[34] H. Hijikata et al. Suppression control method for iron loss of MA-TRIX motor under ux weakening utilizing individual winding current control. In: 2014 International Power Electronics Conference (IPEC-Hiroshima 2014 - ECCE ASIA). 2014, pp. 26732678. doi: 10.1109/IPEC.2014.6869968. 





[35] H. Hijikata et al. Wide range operation by low-voltage inverter-fed MATRIX motor with single-layer distributed winding for automobile traction motor. In: 2015 IEEE Energy Conversion Congress and Exposition (ECCE). 2015, pp. 65456551. doi: 10.1109/ECCE. 2015.7310576. 





[36] D. Hülsmann. Permanentmagneterregte lagerlose Maschinen mit symmetrischen Zahnspulenwicklungen bei Berücksichtigung einer Spaltrohrkapselung. German. PhD thesis. 2012. isbn: 978-3-95404- 210-4. 





[37] C. C. Hwang, S. P. Cheng, and P. L. Li. An Automatic Winding Layout Technique for Permanent Magnet Machines. In: 2007 IEEE International Electric Machines Drives Conference. Vol. 1. 2007, pp. 766769. doi: 10.1109/IEMDC.2007.382764. 





[38] T. Ishigami, Y. Tanaka, and H. Homma. Development of Motor Stator with Rectangular-Wire Lap Winding and an Automatic Process for Its Production. In: Electrical Engineering in Japan 187.4 (2014), pp. 5159. issn: 1520-6416. doi: 10.1002/eej.22522. 





[39] D. Jarrot, Y. Lefevre, and C. Henaux. A tool to help to design windings of permanent magnet synchronous machines. In: 2014 International Conference on Electrical Machines (ICEM). 2014, pp. 19561962. doi: 10.1109/ICELMACH.2014.6960452. 





[40] W. Kauders. Systematik der Drehstromwicklungen. German. In: Elektrotechnik und Maschinenbau 6 (1932), pp. 8892. 





[41] W. Kauders. Systematik der Drehstromwicklungen Teil II. German. In: Elektrotechnik und Maschinenbau 52 (1934), pp. 8592. 





[42] H. J. Kim, D. J. Kim, and J. P. Hong. Characteristic Analysis for Concentrated Multiple-Layer Winding Machine With Optimum Turn Ratio. In: IEEE Transactions on Magnetics 50.2 (2014), pp. 789792. issn: 0018-9464. doi: 10.1109/TMAG.2013.2279100. 





[43] H. Kometani, Y. Asao, and K. Adachi. Dynamo-electric machine. US Patent 6,166,471. 2000. 





[44] S. Kozawa. Trends and Problems in Research of Permanent Magnets for MotorsAddressing Scarcity Problem of Rare Earth Elements. In: Science & Technology Trends 38 (2011), pp. 4054. 





[45] Q. Li et al. A novel multi-layer winding design method for Fractional-Slot Concentrated-Windings Permanent Magnet Machine. In: 2014 IEEE Conference and Expo Transportation Electrication Asia-Pacic (ITEC Asia-Pacic). 2014, pp. 15. doi: 10.1109/ITEC-AP.2014.6940615. 





[46] F. Magnussen and C. Sadarangani. Winding factors and Joule losses of permanent magnet machines with concentrated windings. In: Electric Machines and Drives Conference, 2003. IEMDC'03. IEEE International. Vol. 1. 2003, 333339 vol.1. doi: 10.1109/IEMDC. 2003.1211284. 





[47] J. Mayer, G. Dajaku, and D. Gerling. Mathematical optimization of the MMF-function and -spectrum in concentrated winding machines. In: 2011 International Conference on Electrical Machines and Systems. 2011, pp. 16. doi: 10.1109/ICEMS.2011.6073823. 





[48] J. M. Miller et al. Design considerations for an automotive integrated starter-generator with pole-phase modulation. In: Conference Record of the 2001 IEEE Industry Applications Conference. 36th IAS Annual Meeting (Cat. No.01CH37248). Vol. 4. 2001, 2366 2373 vol.4. doi: 10.1109/IAS.2001.955953. 





[49] G. Müller, K. Vogt, and B. Ponick. Berechnung elektrischer Maschinen. German. John Wiley & Sons, 2008. 692 pp. isbn: 978-3- 527-40525-1. 





[50] H. Mosebach. SYSTEMATIK DREISTRÄNGIGER SYMMETRIS-CHER PM-ERREGTER PPSM. German. Tech. rep. Institute for Electrical Machines, Traction and Drives, TU Braunschweig, 2005. 





[51] E. Nipp. Permanent magnet motor drives with switched stator windings. PhD thesis. Tekniska högskolan i Stockholm. Institutionen för elkraftteknik, 1999. isbn: 99-2975919-0. 





[52] A. Patzak and D. Gerling. Design of a multi-phase inverter for low voltage high power electric vehicles. In: 2014 IEEE International Electric Vehicle Conference (IEVC). 2014, pp. 17. doi: 10.1109/ IEVC.2014.7056143. 





[53] J. Pyrhönen, T. Jokinen, and V. Hrabovcová. Design of Rotating Electrical Machines. John Wiley & Sons, 2009. 





[54] G. Rebora. Dreiphasen-Wicklungen. German. In: Eletrotechnica 18 (1941), p. 72. 





[55] P. B. Reddy, A. M. EL-Refaie, and K. K. Huh. Eect of Number of Layers on Performance of Fractional-Slot Concentrated-Windings Interior Permanent Magnet Machines. In: vol. 30. 4. 2015, pp. 2205 2218. doi: 10.1109/TPEL.2014.2328579. 





[56] P. B. Reddy, K. K. Huh, and A. EL-Refaie. Eect of stator shifting on harmonic cancellation and ux weakening performance of interior PM machines equipped with fractional-slot concentrated windings for hybrid traction applications. In: 2012 IEEE Energy Conversion Congress and Exposition (ECCE). 2012, pp. 525533. doi: 10.1109/ECCE.2012.6342776. 





[57] P. B. Reddy, K. K. Huh, and A. M. EL-Refaie. Generalized Approach of Stator Shifting in Interior Permanent-Magnet Machines Equipped With Fractional-Slot Concentrated Windings. In: IEEE Transactions on Industrial Electronics 61.9 (2014), pp. 50355046. issn: 0278-0046. doi: 10.1109/TIE.2013.2297515. 





[58] R. Richter. Ankerwicklungen für Gleich- und Wechselstrommaschinen: ein Lehrbuch. German. J. Springer, 1920. 





[59] R. Richter. Die Bruchlochwicklungen (Teillochwicklungen) und ihr Entwurf. In: Electrical Engineering (Archiv für Elektrotechnik) 8.6 (1919), pp. 214268. 





[60] S. Sadeghi et al. Wide Operational Speed Range of Five-Phase Permanent Magnet Machines by Using Dierent Stator Winding Congurations. In: IEEE Transactions on Industrial Electronics 59.6 (2012), pp. 26212631. issn: 0278-0046. doi: 10.1109/TIE. 2011.2164771. 





[61] H. Schack-Nielsen. Oberwellenarme Drehstromwicklungen. German. In: Elektrotechnik und Maschinenbau 33/34 (1940), pp. 339 343. 





[62] T. Seike. Die einfache Ausführung der Bruchloch-Ankerwi-cklungen für Wechselstrom. German. In: Elektrotechnik und Maschinenbau 49 (1931), p. 21. 





[63] H. Sequenz. Die Wicklungen elektrischer Maschinen. German. Vol. 1. Springer Verlag, 1950. 





[64] L. Siesing, A. Reinap, and M. Andersson. Thermal properties on high ll factor electrical windings: Inltrated vs non inltrated. In: 2014 International Conference on Electrical Machines (ICEM). 2014, pp. 22182223. doi: 10.1109/ICELMACH.2014.6960492. 





[65] A. C. Smith and D. Delgado. Automated AC winding design. In: Power Electronics, Machines and Drives (PEMD 2010), 5th IET International Conference on. 2010, pp. 16. doi: 10 . 1049 / cp . 2010.0132. 





[66] J. Steinbrink. Design and analysis of windings of electrical machines. In: 2008 International Symposium on Power Electronics, Electrical Drives, Automation and Motion. 2008, pp. 717720. doi: 10.1109/SPEEDHAM.2008.4581183. 





[67] Afang Sun et al. Eect of Multilayer Windings on Rotor Losses of Interior Permanent Magnet Generator With Fractional-Slot Concentrated-Windings. In: Magnetics, IEEE Transactions on 50.11 (2014), pp. 14. 





[68] D. Sun, B. Ge, and D. Bi. Winding design for pole-phase modulation of induction machines. In: 2010 IEEE Energy Conversion Congress and Exposition. 2010, pp. 278283. doi: 10.1109/ECCE. 2010.5618026. 





[69] M. A. Surjanino. Über Mehrphasenwicklungen, bei denen Leiter verschiedener Phasen in einer Nut liegen. German. In: Elektrotechnik und Maschinenbau 49 (June 7, 1931), p. 446. 





[70] M. M. Swamy et al. Extended high-speed operation via electronic winding-change method for AC motors. In: IEEE Transactions on Industry Applications 42.3 (2006), pp. 742752. issn: 0093-9994. doi: 10.1109/TIA.2006.873657. 





[71] Y. Tang. Electromagnetic Fields in Electrical Machines, 2nd Edition. Chinese. Scientic Publisher, 1998. 





[72] N. Tesla. Electro-magnetic motor. Pat. US 381,968 (US). May 1888. 





[73] E. M. Tingley. Two- and Three-Phase Lap Windings in unequal Groups. German. In: The Electrical Review and Western Electrician 66 (1915), p. 166. 





[74] A. O. Di Tommaso, F. Genduso, and R. Miceli. A platform independent software for the design and analysis of windings of rotating electrical machines. In: 2014 16th International Power Electronics and Motion Control Conference and Exposition. 2014, pp. 1324 1330. doi: 10.1109/EPEPEMC.2014.6980696. 





[75] A. O. Di Tommaso, F. Genduso, and R. Miceli. A software for the evaluation of winding factor harmonic distribution in high e- ciency electrical motors and generators. In: 2013 Eighth International Conference and Exhibition on Ecological Vehicles and Renewable Energies (EVER). 2013, pp. 16. doi: 10.1109/EVER.2013. 6521571. 





[76] A. O. Di Tommaso et al. Assisted software design of a wide variety of windings in rotating electrical machinery. In: 2014 Ninth International Conference on Ecological Vehicles and Renewable Energies (EVER). 2014, pp. 16. doi: 10.1109/EVER.2014.6844095. 





[77] H. Traÿl. Polumschaltbare Wicklungen für Synchronmaschinen mit ausgeprägten Polen. German. In: Elektrotechnik und Maschinenbau 58 (1940), p. 145. 





[78] C. Veeh. Oberwellenorientierte Wicklungsmodikation von permanentmagneterregten Synchronmaschinen mit Zahnspulenwicklung. German. PhD thesis. 2013. isbn: 978-3-18-340821-4. 





[79] G. von Pngsten et al. Inuence of Winding Scheme on the Iron-Loss Distribution in Permanent Magnet Synchronous Machines. In: IEEE Transactions on Magnetics 50.4 (2014), pp. 14. issn: 0018-9464. doi: 10.1109/TMAG.2013.2288433. 





[80] J. Wang et al. Design Considerations for Tubular Flux-Switching Permanent Magnet Machines. In: IEEE Transactions on Magnetics 44.11 (2008), pp. 40264032. issn: 0018-9464. doi: 10.1109/ TMAG.2008.2002773. 





[81] Y. Wang, R. Qu, and J. Li. Multilayer Windings Eect on Interior PM Machines for EV Applications. In: IEEE Transactions on Industry Applications 51.3 (2015), pp. 22082215. issn: 0093-9994. doi: 10.1109/TIA.2014.2385934. 





[82] D. C. White and H. H. Woodson. Electromechanical Energy Conversion. Wiley, 1959. 





[83] K. Widdmann. Entwurf von Bruchlochwicklungen. In: Elektrotechnik und Maschinenbau 64 (1947), p. 83. 





[84] Wikipedia. Rotational symmetry. [Online; accessed 16-October-2016]. 2016. url: https : / / en . wikipedia . org / wiki / Rotational _ symmetry. 





[85] P. Zhou et al. Determination of d  q Axis Parameters of Interior Permanent Magnet Machine. In: IEEE Transactions on Magnetics 46.8 (2010), pp. 31253128. issn: 0018-9464. doi: 10.1109/TMAG. 2010.2043507. 



# Nomenclature

# Mathematical Notations

${ \mathbf { } } ^ { a , }$ A algebraical vector 

${ \pmb a } ^ { \mathrm { T } } , { \pmb A } ^ { \mathrm { T } }$ transpose of vector a, A 

${ \hat { a } } , { \hat { A } }$ amplitude of a sinusoidal function 

A matrix 

AT ${ \bf A } ^ { \mathrm { T } }$ transpose of matrix A 

$\operatorname { I m } \{ \underline { { a } } \}$ imaginal part of the complex number a 

$\mathrm { R e } \{ \underline { { a } } \}$ real part of the complex number $\underline { { a } }$ 

${ \overline { { a } } } , { \overline { { A } } }$ mean value 

$\underline { { a } } , \underline { { A } }$ complex number 

$\vec { a }$ Physical vector 

f (x) function with variable x 

# Mathematical Functions

abs(a) magnitude of the complex number $\underline { { a } }$ 

ceil(a) nearest integer greater than or euqal to a 

floor(a) the nearest integer less than or equal to $a$ 

lcm(a, b) least common multiplier of a and b 

mod(a, b) the modular after $a / b$ 

sign(a) sign of the vector a 

size(a) number of element of the vector a 


Symbols


<table><tr><td><eq>\alpha, \beta</eq></td><td>Angle, general</td></tr><tr><td><eq>\phi</eq></td><td>m-phase current system as vector</td></tr><tr><td><eq>\epsilon, \epsilon</eq></td><td>Error</td></tr><tr><td><eq>\psi</eq></td><td>Vector of phase flux-linkage</td></tr><tr><td><eq>J&#x27;_{\Omega}</eq></td><td>Jacobian vector of the magnetic co-energy in respect of mechanical variation</td></tr><tr><td><eq>J&#x27;_{i}</eq></td><td>Jacobian matrix of the magnetic co-energy in respect of electrical variation</td></tr><tr><td><eq>J_{\Omega}</eq></td><td>Jacobian vector of the magnetic energy in respect of mechanical variation</td></tr><tr><td><eq>J_{i}</eq></td><td>Jacobian matrix of the magnetic energy in respect of electrical variation</td></tr><tr><td><eq>m^{CD}</eq></td><td>Vector used for the calculation of the classical double-layer winding topology</td></tr><tr><td><eq>m^{MCond}</eq></td><td>Vector used for the calculation of the multi-conductor winding topology</td></tr><tr><td><eq>m_{c}</eq></td><td>Connection vector</td></tr><tr><td><eq>m_{c}^{MT}</eq></td><td>Connection vector of the multi-turn winding topology</td></tr><tr><td><eq>N_{c}^{MCond}</eq></td><td>Number of the conductors of the negative coil sides of the multi-conductor winding topology</td></tr><tr><td><eq>w</eq></td><td>Vector used for presentation of the winding topology</td></tr><tr><td><eq>w_{c}^{MC}</eq></td><td>Number of turns of the coils of the multi-coil winding topology</td></tr><tr><td><eq>w_{c}^{ML}</eq></td><td>Number of turns of the coils of the multi-Layer winding topology</td></tr><tr><td><eq>w_{c}^{MT}</eq></td><td>Number of turns of the coils of the multi-turn winding topology</td></tr><tr><td><eq>\Delta T_{w}</eq></td><td>Temperatur difference of the winding</td></tr></table>

$\delta$ Air gap thickness 

$\delta ( x )$ Dirac impulse function 

$\gamma$ Working harmonic order 

Bˆr,ν $\hat { B } _ { r , \nu }$ Rotor ux density amplitude of the ν-harmonic order 

Kˆs,ν $\hat { K } _ { s , \nu }$ Stator current sheet amplitude of the ν-harmonic order 

$\kappa _ { c }$ Thermal specic conductivity of the conductor 

$\kappa _ { p }$ κp Thermal specic conductivity of the isolation 

$\kappa _ { w , t h }$ Thermal specic conductivity of the winding 

$\mathbb { U } _ { \overline { { c } } }$ Set of phase winding 

MMCond Matrix used for the calculation of the multi-conductor winding topology 

$\mathbf { M } _ { \nu }$ Transformation matrix between space and spectrum domain 

$\mathbf { M } _ { c }$ Connection matrix 

$\mathbf { M } _ { c } ^ { \mathrm { C D } }$ Connection Matrix of the classical double-layer winding topology 

$\mathbf { M } _ { c } ^ { \mathrm { D } }$ Connection matrix of the double-way connection 

$\mathbf { M } _ { c } ^ { \mathrm { M T } }$ Connection matrix of the multi-turn winding topology 

$\mathbf { M } _ { c } ^ { \mathrm { S , M D } }$ Connection matrix of the Single-way connection of minima deviation 

$\mathbf { M } _ { c } ^ { \mathrm { S } , \mathrm { S P } }$ Connection matrix of the single-way connection of shortest path 

MS,MD $\mathbf { M } _ { c , s } ^ { \mathrm { S , M D } }$ c,s Connection matrix of the Single-way connection of minima deviation for the single-layer winding topology 

$\mathbf { M } _ { c , s } ^ { \mathrm { S } , \mathrm { S P } }$ Connection matrix of the single-way connection of shortest path for the single-layer winding topology 

R Resistance matrix 

${ \bf S } _ { \mathrm { M } , 1 }$ Matrix for the calculation of the lower symmetry part 

${ \bf S } _ { \mathrm { M , u } }$ Matrix for the calculation of the upper symmetry part 

${ \bf { S } } _ { \mathrm { { M } } }$ Matrix of mirror symmetry 

$\mathbf { S } _ { \mathrm { R } }$ Matrix of rotation symmetry 

(rect)(x) Rectangle-shaped function 

$_ i$ vector of phase current 

$\textbf { \em u }$ vector of phase voltage 

$\mathbf { J } _ { \Omega }$ Jacobian matrix in respective of mechanical variation 

$\mathbf { J } _ { i }$ Jacobian matrix in respective of electrical variation 

C Conductor distribution matrix 

$\overline { { \mathbf { C } } } _ { s }$ Normalized conductor distribution matrix of the single-layer wining topology 

ν Harmonic order, general 

$\omega$ Electrical frequency 

$\overline { { \overline { { \mathbf { C } } } } }$ normalized conductor distribution matrix 

A, B, C Phase current with negative winding direction 

$\overline { { f } }$ Average force density 

$\overline { { c } } _ { s } ^ { \mathrm { R , M } }$ Normalized conductor distribution vector of the single-layer wining topology after the rotation and mirror symmetry exploitation 

Θ Normalized MMF vector 

$\overline { { c } } ^ { \mathrm { R , M } }$ Normalized conductor distribution vector after rotation and mirror symmetry exploitation 

$\overline { { c } } ^ { \mathrm { R } }$ Normalized conductor distribution vector after rotation symmetry exploitation 

$\overline { { \boldsymbol { c } } } _ { h }$ h-th phase winding 

<table><tr><td><eq>\overline{\mathbf{c}}_k</eq></td><td>k-th column vector of the normalized conductor distribution matrix</td></tr><tr><td><eq>\overline{\mathbf{c}}_n</eq></td><td>n-th row vector of the normalized conductor distribution matrix</td></tr><tr><td><eq>\phi_k</eq></td><td>Current phase of the k-th phase current</td></tr><tr><td><eq>\vec{E}_v</eq></td><td>Electrical field streght caused by mechanical velocity</td></tr><tr><td><eq>\vec{F}</eq></td><td>Electromechanical Force</td></tr><tr><td><eq>\vec{l}</eq></td><td>Length with direction</td></tr><tr><td><eq>\vec{v}</eq></td><td>Mechanical velocity</td></tr><tr><td><eq>\rho</eq></td><td>Electrical specific resistance</td></tr><tr><td><eq>\tau_c</eq></td><td>Coil pitch</td></tr><tr><td><eq>\tau_{so}</eq></td><td>Slot opening</td></tr><tr><td><eq>\tau_{sp}</eq></td><td>Slot pitch</td></tr><tr><td><eq>\underline{\Theta}</eq></td><td>Total slot MMF as vector</td></tr><tr><td><eq>\underline{\Theta}_{\nu}</eq></td><td>MMF harmonic of <eq>\nu</eq>-th order</td></tr><tr><td><eq>\underline{u}</eq></td><td>Complex voltage phasor as vector</td></tr><tr><td><eq>\underline{\Theta}</eq></td><td>Complex phasor of MMF</td></tr><tr><td><eq>\underline{C}_{\nu}</eq></td><td>Fourier coefficient of the <eq>\nu</eq>-th harmonic</td></tr><tr><td><eq>\vec{A}</eq></td><td>Magnetic vector potential</td></tr><tr><td><eq>\vec{a}, \vec{a}</eq></td><td>Physical vector</td></tr><tr><td><eq>\vec{B}</eq></td><td>Magnetic flux density</td></tr><tr><td><eq>\vec{E}</eq></td><td>Eletric field strength</td></tr><tr><td><eq>\vec{H}</eq></td><td>Magnetic field strength</td></tr><tr><td><eq>\vec{J}</eq></td><td>Current density</td></tr><tr><td><eq>\vec{S}</eq></td><td>Surface with direction vector</td></tr></table>

$\vec { \Omega }$ Mechanical rotation speed 

$\vec { \pmb { T _ { q } } }$ Electromagnetic torque 

$\xi _ { \nu }$ Winding factor of the ν-harmonic order 

$\xi _ { n } u ^ { n }$ The n-th part winding factor of the νth-harmonic 

A, B, C Phase current with positive winding direction 

$A _ { z }$ Z-component of the vector potential 

$b$ Number of coils per coil group 

c Conductor charaterized number 

$D _ { \delta }$ Diameter of the air gap 

$E _ { m } ^ { \prime }$ Magnetic co-energy 

$E _ { \Omega }$ Mechanical energy 

$E _ { d i s s }$ dissipative energy 

Ee,c $E _ { e , c }$ Coupling electrical energy 

$E _ { e , d }$ Dissipative electrical energy 

$E _ { e }$ Electrical energy 

$E _ { m }$ Magnetic energy 

$f$ Distance between adjacent coils 

$f _ { c }$ Filling factor of the conductor 

$f _ { p }$ Filling factor of the isolation 

$g , z$ Integer, general 

$j$ Imaginary unit 

$J _ { z }$ Z-component of the current densigy 

K Number of coil groups 

k, n Index, general 

$l _ { c }$ Circumference of the machine 

$l _ { z }$ Lenght in z-direction 

m Number of phases 

$N _ { l }$ Number of winding layers 

$N _ { s }$ Number of slots 

$N _ { w }$ Number of possible winding topology 

$N _ { \overline { { c } } , n }$ Number of negative conductor distribution 

$N _ { \overline { { c } } , p }$ Number of positive conductor distribution 

$N _ { \overline { { c } } }$ Number of conductor distribution 

$N _ { c , k }$ Number of conductors belonging to k-th phase winding 

$O _ { c , k }$ Winding direction of conductors belong to k-th phase winding 

p Number of poles 

$P _ { l o s s , w }$ Power loss of the winding 

q Number of slot per pole per phase 

$R _ { e l , c }$ Electrical resistance of the conductor 

$R _ { e l , w }$ Electrical resistance of the winding 

Rth,w $R _ { t h , w }$ Thermal resistance of the winding 

$S _ { n }$ Area of the nth-slot 

sn $s _ { n }$ Area, general 

t Time 

un $u _ { n }$ Induced voltage in the n-th slots 

V Volumes 

$w _ { c }$ Number of turns of coil 

wk $w _ { k }$ Total number of turns of the k-th phase winding 

$x$ Coil pitch 

$x , y , z$ Space coordinate 

y Distance between adjacent coil groups 

$Z _ { 1 } , Z _ { 2 }$ Number of coil groups within the positive and negative winding zone 

# Acronyms

EMF Electro-Motive Force 

MMF Magneto-Motive Force 

# List of Figures

1.1. The electrical machine as an electromechanical energy converter 2 

1.2. Dierent methods for the calculation of the electrical coupling energy by xed rotor position (for the illustration only one component of the eld quantities is used) . . . . 8 

1.3. The double roles of the multi-phase symmetrical winding 9 

2.1. impacts of the winding insulation on the power density and eciency of the machine [32] 11 

2.2. impacts of the number of turns on the max. speed-torque operation curve [70] 12 

2.3. Impacts of the winding production method on slot lling factor [1] . . . 13 

2.4. Impacts of the winding production method on the endwinding [38] . . 14 

2.5. Impacts of the winding topology on the torque-speed operation range [22] 16 

2.6. Impacts of the winding topology on the d/q-inductances [22] 17 

2.7. Impacts of the winding topology on the iron loss of surface PM machine [28] 19 

2.8. Impacts of the over-harmonic winding topology on the iron loss of interior PM machine [22] . . 19 

2.9. Impacts of the fundamental harmonic winding topology on the iron loss of interior PM machine [79] . . 20 

2.10. Impacts of the winding topology on the surface permanent magnet eddy current losses [20] 21 

2.11. Impacts of the winding topology on the interior permanent magnet eddy current losses [22] 22 

4.1. Methods for winding topology treatment: the theoretical framework . . . 37 

4.2. The investigated winding topologies 39 

4.3. The winding factor harmonic spectrum of the winding topology given in gure 4.2, calculated by using the composite approach . . . 42 

4.4. The hierarchical structure of the phase winding given in gure 4.2b . . 43 

4.5. Illustration of the distance between coil groups . . . . . . 45 

4.6. The winding factor harmonic spectrum for the winding topologies given in gure 4.2 calculated by using the decomposite approach 47 

4.7. The winding factor harmonic spectrum of the over-harmonic winding calculated by using dierent characteristic parameters . 48 

4.8. The winding factor spectrum calculated by using the MMF analysis. blue: MMF assumed as Dirac delta function, lime: MMF assumed as rectangle-shaped function over the slot opening, red: MMF assumed as rectangle-shaped function over the slot pitch . . 54 

4.9. The working harmonic dependent star of slots for a winding with 12 slots . . 57 

4.10. The sector of the 3-phase current system 58 

4.11. Merge the star of slots (gure 4.9) and the sector of the 3-phase current system (gure 4.10) 58 

4.12. The single layer winding topology . . . . . 59 

4.13. The double layer winding topology . . . 60 

4.14. Deduction of the Tingley schema from the star of slots diagram . 61 

4.15. Set-up the star of slots diagram by using dierent methods. Top: method introduced by R. Richter, bottom: method introduced by V. Bedjanic . 62 

4.16. Design results of a 3-phase double-layer winding with 12 slots and the 5-th harmonic as working harmonic by using the Kauders' method . . 67 

4.17. Illustration of the winding design method introduced by D. H. Braymer and A. C. Roe . . 68 

4.18. The design procedure by using stochastic approach . . . . 69 

4.19. The Design Parameters of the stochastic approach . . . . 70 

4.20. The multi-layer modication approach . . . 74 

4.21. The multi-slot modication approach . . . 75 

4.22. The multi-turn modication approach . . . 76 

4.23. The multi-conductor modication approach . . . . . . . . 77 

4.24. The multi-coil approach . . . 78 

5.1. A novel representation form of the winding factor harmonic spectrum with the periodicity of the winding factor harmonic spectrum automatically included by the periodicity of the polar coordinate system . . 88 

5.2. Illustration of the normalized MMF distribution with 12 slots. Each MMF phasor has an index, indicating its slot position. . 89 

5.3. Illustration of the symmetrical multi-phase current system 91 

5.4. Illustration of the normalized conductor distribution matrix of the fundamental and the over-harmonic winding with 12 slots and 3 phases . . . 93 

5.5. The real and ideal winding factor harmonic spectrum with γ = 5 . . 96 

5.6. The real and ideal normalized MMF distribution with working harmonic γ = 5 . . 97 

5.7. Types of winding topology for winding of 12 slots and 3 phases . . . . 101 

5.8. Illustration of the projection of one MMF phasor (the ideal MMF phasor in the rst slot, assigned with index 0) on the symmetrical multi-phase current system . 103 

5.9. Illustration of the normalized conductor distribution matrix C to underline its symmetrical properties . . . . . . . 104 

5.10. The mirror symmetry of the primitive phase winding topology . . 107 

5.11. The conductor distributions within a primitive coil group and the corresponding double- and single-way connections 111 

5.12. Derivation of multi-turn and multi-layer winding topology 114 

5.13. Derivation of the multi-coil and multi-conductor winding topology . . 115 

5.14. Derivation of the double-layer winding topology . . . . . . 118 

5.15. Derivation of the single-layer winding topology . . . . . . 119 

5.16. Evaluation of the winding topology . . . . 121 

5.16. Evaluation of the winding topology . . . . 122 

5.16. Evaluation of the winding topology . . . . . 123 

5.16. Evaluation of the winding topology . . . . . 124 

6.1. The design parameters . . . 126 

6.2. The ideal winding factor harmonic spectrum . . . . . . . . 127 

6.3. The ideal normalized MMF distribution . . . . . . . 127 

6.4. The rst type of normalized conductor distribution matrix and primitive double layer winding for the case of $\gamma = 1$ . 129 

6.5. The second type of normalized conductor distribution matrix and primitive double layer winding for the case of $\gamma = 1 1 3 0$ 

6.6. The rst type of normalized conductor distribution matrix and primitive double layer winding for the case of $\gamma = 5$ . 131 

6.7. The second type of normalized conductor distribution matrix and primitive double layer winding for the case of $\gamma = 5 1 3 2$ 

6.8. The rotational symmetry and the primitive single phase winding for the case of $\gamma = 1$ . 134 

6.9. The rotational symmetry and the primitive single phase winding for the case of $\gamma = 5$ . . . . . 135 

6.10. The mirror symmetry and the primitive group for the case of $\gamma = 1$ . . 137 

6.11. The mirror symmetry and the primitive coil group for the case of $\gamma = 5$ . . 138 

6.12. The connection matrix and the primitive coils of the fundamental harmonic winding of $\gamma = 1$ . . . . . 140 

6.13. The connection matrix and the primitive coils of the overharmonic winding of $\gamma = 5$ . . . . 141 

6.14. The multi-turn (left) and multi-layer (right) winding topology of the fundamental harmonic winding . . . . . . . 143 

6.15. The multi-turn (left) and multi-layer (right) winding topology of the over-harmonic winding . . 144 

6.16. The multi-coil (left) and multi-conductor (right) winding topology of the fundamental harmonic winding . . . . . . 146 

6.17. The multi-coil (left) and multi-conductor (right) winding topology of the over-harmonic winding . . . . 147 

6.18. The classical double-layer winding topology of the fundamental harmonic winding . 149 

6.19. The classical double-layer winding topology of the overharmonic winding . . . . . . 150 

6.20. The classical single-layer winding topology of the fundamental harmonic winding . 152 

6.21. The classical single-layer winding topology of the overharmonic winding . . . . 153 

6.22. The classical single-layer winding topology . . . . . . . . . 154 

6.23. The double-layer winding topology . . . . 155 

6.23. The double-layer winding topology . . . . 156 

6.24. The multi-coil winding topology . . . . . . 158 

6.25. The multi-conductor winding topology . . . . . . 159 

6.26. The classical single-layer winding topology . . . . . . . . . 160 

6.27. The double-layer winding topology . . . . 161 

6.27. The double-layer winding topology . . . . 162 

6.28. The multi-turn winding topology . . . . 163 

6.29. The multi-layer winding topology . . . . 164 

6.30. The multi-coil winding topology . . . . 165 

6.31. The multi-conductor winding topology . . . . . . 166 

6.32. The winding factor of the fundamental harmonic vs. the conductor ratio . 167 

6.33. The rst type of the normalized conductor distribution matrix and the primitive double layer winding . . . . . . . 168 

6.34. The second type of the normalized conductor distribution matrix and the primitive double layer winding . . . . . . . 169 

6.35. The primitive single phase winding and the primitive coil group . 171 

6.36. The double- and single-way connections: double-way connection (left), single-way connection of minimal deviation (middle), single-way connection of shortest path (right) . 172 

6.37. The multi-turn winding topology . . . . 174 

6.38. The multi-layer winding topology . . . . 175 

6.39. The Single-layer winding topology with unique number of conductors per slot . . . 176 

6.40. The classical double-layer winding topology . . . . . . . . 177 

6.41. The multi-coil winding topology . . . . . 177 

6.42. The multi-conductor winding topology . . . . . . . . . . . 178 

6.43. The rst type of normalized conductor distribution matrix and the primitive double layer winding . 180 

6.44. The second type of normalized conductor distribution matrix and the primitive double layer winding 181 

6.45. The primitive single phase winding and the primitive coil group . 182 

6.46. The double- and single-way connections: double-way connection (left), single-way connection of minimal deviation (middle), single-way connection of shortest path (right) . 183 

6.47. The classical double-layer winding . . 185 

6.48. The novel multi-layer, multi-turn and multi-coil winding . 185 