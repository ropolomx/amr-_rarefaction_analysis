#! /usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3_unweighted

def prepare_kraken(kraken):

    kraken['SampleName'] = kraken['Sample'].str.split('_').str[0]+'_'+kraken['Sample'].str.split('_').str[1]

    kraken['Type'] = kraken['SampleName'].str.split('_').str[1]

    kraken['Type'] = kraken['Type'].str.replace('2','')

    kraken[kraken['Kraken.ID'] == 374840]

    # Remove phiX and microviridae reads

    kraken = kraken.drop(kraken['Kraken.ID'] == 374840)
    kraken = kraken.drop(kraken['Kraken.ID'] == 10842)
    kraken = kraken.drop(kraken['Kraken.ID'] == 10841)

# Remove

def categoryDiffKraken(category):
    full = krakenConcat.loc[(krakenConcat['TaxLevel'] == category) & (krakenConcat['Sample_Type'] =="F"), "Name"]
    half = krakenConcat.loc[(krakenConcat['TaxLevel'] == category) & (krakenConcat['Sample_Type'] == "H"), "Name"]
    quar = krakenConcat.loc[(krakenConcat['TaxLevel'] == category) & (krakenConcat['Sample_Type'] == "QD"), "Name"]
    setfull = set(full)
    sethalf = set(half)
    setquar = set(quar)
    return(setfull, sethalf, setquar)

def categoryDiffAMR(category):
    full = amrResults[category][amrResults['Sample_type'] == "D1"]
    half = amrResults[category][amrResults['Sample_type'] == "D0.5"]
    quar = amrResults[category][amrResults['Sample_type'] == "D0.25"]
    seqtk = amrResults[category][amrResults['Sample_type'] == "D0.25_seqtk"]
    setfull = set(full)
    sethalf = set(half)
    setquar = set(quar)
    setseqtk = set(seqtk)
    return(setfull, sethalf, setquar, setseqtk)

allTaxa = ['P', 'C', 'F', 'O', 'G', 'S']

allTaxaSets = {}

for t in allTaxa:
    allTaxaSets[t] = categoryDiffKraken(t)

familyFullSet = allTaxaSets['F'][0]
familyHalfSet = allTaxaSets['F'][1]
familyQuarSet = allTaxaSets['F'][2]
familySets = [familyFullSet, familyHalfSet, familyQuarSet]

classFullSet = allTaxaSets['C'][0]
classHalfSet = allTaxaSets['C'][1]
classQuarSet = allTaxaSets['C'][2]
classSets = [classFullSet, classHalfSet, classQuarSet]

orderFullSet = allTaxaSets['O'][0]
orderHalfSet = allTaxaSets['O'][1]
orderQuarSet = allTaxaSets['O'][2]
orderSets = [orderFullSet, orderHalfSet, orderQuarSet]

phylumFullSet = allTaxaSets['P'][0]
phylumHalfSet = allTaxaSets['P'][1]
phylumQuarSet = allTaxaSets['P'][2]
phylumsets = [phylumFullSet, phylumHalfSet, phylumQuarSet]


genusFullSet = allTaxaSets['G'][0]
genusHalfSet = allTaxaSets['G'][1]
genusQuarSet = allTaxaSets['G'][2]
genusSets = [genusFullSet, genusHalfSet, genusQuarSet]


speciesFullSet = allTaxaSets['S'][0]
speciesHalfSet = allTaxaSets['S'][1]
speciesQuarSet = allTaxaSets['S'][2]
speciesSets = [speciesFullSet, speciesHalfSet, speciesQuarSet]

v3Phylum = venn3_unweighted(phylumSets, ('D1', 'D0.5', 'D0.25'))
plt.title('Phylum')
plt.savefig('krakenPhylumVenn.png')
plt.clf()
plt.cla()

v3Order = venn3_unweighted(orderSets, ('D1', 'D0.5', 'D0.25'))
plt.title('Order')
plt.savefig('krakenOrderVenn.png')
plt.clf()
plt.cla()

v3Family = venn3_unweighted(familySets, ('D1', 'D0.5', 'D0.25'))
plt.title('Family')
plt.savefig('krakenFamilyVenn.png')
plt.clf()
plt.cla()

v3Class = venn3_unweighted(classSets, ('D1', 'D0.5', 'D0.25'))
plt.title('Class')
plt.savefig('krakenClassVenn.png')
plt.clf()
plt.cla()

v3Genus = venn3_unweighted(genusSets, ('D1', 'D0.5', 'D0.25'))
plt.title('Genus')
plt.savefig('krakenGenusVenn.png')
plt.clf()
plt.cla()

v3Species = venn3_unweighted(speciesSets, ('D1', 'D0.5', 'D0.25'))
plt.title('Species')
plt.savefig('krakenSpeciesVenn.png')
plt.clf()
plt.cla()

# Building AMR Venn diagrams

allAMRCats = ['Class', 'Mechanism', 'Group', 'Name']

allAMRCatsSets = {}

for c in allAMRCats:
    allAMRCatsSets[c] = categoryDiffAMR(c)

classFullSet = allAMRCatsSets['Class'][0]
classHalfSet = allAMRCatsSets['Class'][1]
classQuarSet = allAMRCatsSets['Class'][2]
classSeqtkSet = allAMRCatsSets['Class'][3]
classSets = [classFullSet, classHalfSet, classQuarSet, classSeqtkSet]

mechFullSet = allAMRCatsSets['Mechanism'][0]
mechHalfSet = allAMRCatsSets['Mechanism'][1]
mechQuarSet = allAMRCatsSets['Mechanism'][2]
mechSeqtkSet = allAMRCatsSets['Mechanism'][3]
mechSets = [mechFullSet, mechHalfSet, mechQuarSet, mechSeqtkSet]

groupFullSet = allAMRCatsSets['Group'][0]
groupHalfSet = allAMRCatsSets['Group'][1]
groupQuarSet = allAMRCatsSets['Group'][2]
groupSeqtkSet = allAMRCatsSets['Group'][3]
groupSets = [groupFullSet, groupHalfSet, groupQuarSet, groupSeqtkSet]

geneFullSet = allAMRCatsSets['Name'][0]
geneHalfSet = allAMRCatsSets['Name'][1]
geneQuarSet = allAMRCatsSets['Name'][2]
geneSeqtkSet = allAMRCatsSets['Name'][3]
geneSets = [geneFullSet, geneHalfSet, geneQuarSet, geneSeqtkSet]

v3class = venn3_unweighted(classSets[0:2], ('D1', 'D0.5', 'D0.25'))
plt.title('Class')
plt.savefig('amrClassVenn.png')
plt.clf()
plt.cla()

v3mech = venn3_unweighted(mechSets[0:2], ('D1', 'D0.5', 'D0.25'))
plt.title('Mech')
plt.savefig('amrMechVenn.png')
plt.clf()
plt.cla()

v3group = venn3_unweighted(groupSets[0:2], ('D1', 'D0.5', 'D0.25'))
plt.title('Group')
plt.savefig('amrGroupVenn.png')
plt.clf()
plt.cla()

v3gene = venn3_unweighted(geneSets[0:2], ('D1', 'D0.5', 'D0.25'))
plt.title('Gene')
plt.savefig('amrGeneVenn.png')
plt.clf()
plt.cla()


v3species = venn3_unweighted(speciesSets[0:2], ('D1', 'D0.5', 'D0.25'))
plt.title('Species')
plt.savefig('amrSpeciesVenn.png')
plt.clf()
plt.cla()


def setOperations():
    """Generate a file with all the results of the set operations
    Ideally return a table with the results"""

geneAllIntersects = geneFullSet.intersection(geneHalfSet).intersection(geneQuarSet)
geneFullDiffHalf = geneFullSet.difference(geneHalfSet)
geneFullDiffQuar = geneFullSet.difference(geneQuarSet)
geneFullInterHalfDiffQuar = geneFullSet.intersection(geneHalfSet).difference(geneQuarSet)
geneHalfDiffFull = geneHalfSet.difference(geneFullSet)
geneHalfDiffQuar = geneHalfSet.difference(geneQuarSet)
geneHalfInterQuarDiffFull = geneHalfSet.intersection(geneFullSet).difference(geneFullSet)
geneQuarDiffFull = geneQuarSet.difference(geneFullSet)
geneQuarDiffHalf = geneQuarSet.difference(geneHalfSet)
geneQuarInterFullDiffHalf = geneQuarSet.intersection(geneFullSet).difference(geneHalfSet)


classAllIntersects = classFullSet.intersection(classHalfSet).intersection(classQuarSet)
classFullDiffHalf = classFullSet.difference(classHalfSet)
classFullDiffQuar = classFullSet.difference(classQuarSet)
classFullInterHalfDiffQuar = classFullSet.intersection(classHalfSet).difference(classQuarSet)
classHalfDiffFull = classHalfSet.difference(classFullSet)
classHalfDiffQuar = classHalfSet.difference(classQuarSet)
classHalfInterQuarDiffFull = classHalfSet.intersection(classFullSet).difference(classFullSet)
classQuarDiffFull = classQuarSet.difference(classFullSet)
classQuarDiffHalf = classQuarSet.difference(classHalfSet)
classQuarInterFullDiffHalf = classQuarSet.intersection(classFullSet).difference(classHalfSet)


groupAllIntersects = groupFullSet.intersection(groupHalfSet).intersection(groupQuarSet)
groupFullDiffHalf = groupFullSet.difference(groupHalfSet)
groupFullDiffQuar = groupFullSet.difference(groupQuarSet)
groupFullInterHalfDiffQuar = groupFullSet.intersection(groupHalfSet).difference(groupQuarSet)
groupHalfDiffFull = groupHalfSet.difference(groupFullSet)
groupHalfDiffQuar = groupHalfSet.difference(groupQuarSet)
groupHalfInterQuarDiffFull = groupHalfSet.intersection(groupFullSet).difference(groupFullSet)
groupQuarDiffFull = groupQuarSet.difference(groupFullSet)
groupQuarDiffHalf = groupQuarSet.difference(groupHalfSet)
groupQuarInterFullDiffHalf = groupQuarSet.intersection(groupFullSet).difference(groupHalfSet)


mechAllIntersects = mechFullSet.intersection(mechHalfSet).intersection(mechQuarSet)
mechFullDiffHalf = mechFullSet.difference(mechHalfSet)
mechFullDiffQuar = mechFullSet.difference(mechQuarSet)
mechFullInterHalfDiffQuar = mechFullSet.intersection(mechHalfSet).difference(mechQuarSet)
mechHalfDiffFull = mechHalfSet.difference(mechFullSet)
mechHalfDiffQuar = mechHalfSet.difference(mechQuarSet)
mechHalfInterQuarDiffFull = mechHalfSet.intersection(mechFullSet).difference(mechFullSet)
mechQuarDiffFull = mechQuarSet.difference(mechFullSet)
mechQuarDiffHalf = mechQuarSet.difference(mechHalfSet)
mechQuarInterFullDiffHalf = mechQuarSet.intersection(mechFullSet).difference(mechHalfSet)

geneSets = [geneAllIntersects,
geneFullDiffHalf,
geneFullDiffQuar,
geneFullInterHalfDiffQuar,
geneHalfDiffFull,
geneHalfDiffQuar,
geneHalfInterQuarDiffFull,
geneQuarDiffFull,
geneQuarDiffHalf,
geneQuarInterFullDiffHalf]

classSets = [classAllIntersects,
classFullDiffHalf,
classFullDiffQuar,
classFullInterHalfDiffQuar,
classHalfDiffFull,
classHalfDiffQuar,
classHalfInterQuarDiffFull,
classQuarDiffFull,
classQuarDiffHalf,
classQuarInterFullDiffHalf]

mechSets = [mechAllIntersects,
mechFullDiffHalf,
mechFullDiffQuar,
mechFullInterHalfDiffQuar,
mechHalfDiffFull,
mechHalfDiffQuar,
mechHalfInterQuarDiffFull,
mechQuarDiffFull,
mechQuarDiffHalf,
mechQuarInterFullDiffHalf]

groupSets = [groupAllIntersects,
groupFullDiffHalf,
groupFullDiffQuar,
groupFullInterHalfDiffQuar,
groupHalfDiffFull,
groupHalfDiffQuar,
groupHalfInterQuarDiffFull,
groupQuarDiffFull,
groupQuarDiffHalf,
groupQuarInterFullDiffHalf]


geneSetLengths = [len(g) for g in geneSets]
classSetLengths = [len(c) for c in classSets]
mechSetLengths = [len(m) for m in mechSets]
groupSetLengths = [len(g) for g in groupSets]

geneLists = [list(g) for g in geneSets]
classLists = [list(c) for c in classSets]
mechLists = [list(m) for m in mechSets]
groupLists = [list(g) for g in groupSets]

amrGeneSetOperationsTuple = zip(setOperationKeys, geneSetLengths, geneLists)
amrClassSetOperationsTuple = zip(setOperationKeys, classSetLengths, classLists)
amrMechSetOperationsTuple = zip(setOperationKeys, mechSetLengths, mechLists)
amrGroupSetOperationsTuple = zip(setOperationKeys, groupSetLengths, groupLists)

amrGeneUniqueDF = pd.DataFrame.from_records(amrGeneSetOperationsTuple, columns=['Comparison', 'Size', 'Members'])
amrClassUniqueDF = pd.DataFrame.from_records(amrClassSetOperationsTuple, columns=['Comparison', 'Size', 'Members'])
amrMechUniqueDF = pd.DataFrame.from_records(amrMechSetOperationsTuple, columns=['Comparison', 'Size', 'Members'])
amrGroupUniqueDF = pd.DataFrame.from_records(amrGroupSetOperationsTuple, columns=['Comparison', 'Size', 'Members'])

amrGeneUniqueDF.to_csv('amrGeneSetOperations.csv', index = False)
amrClassUniqueDF.to_csv('amrClassSetOperations.csv', index = False)
amrMechUniqueDF.to_csv('amrMechSetOperations.csv', index = False)
amrGroupUniqueDF.to_csv('amrGroupSetOperations.csv', index = False)


def krakenSetOperations():
    """Generate a file with all the results of the set operations
    Ideally return a table with the results"""

speciesAllIntersects = speciesFullSet.intersection(speciesHalfSet).intersection(speciesQuarSet)
speciesFullDiffHalf = speciesFullSet.difference(speciesHalfSet)
speciesFullDiffQuar = speciesFullSet.difference(speciesQuarSet)
speciesFullInterHalfDiffQuar = speciesFullSet.intersection(speciesHalfSet).difference(speciesQuarSet)
speciesHalfDiffFull = speciesHalfSet.difference(speciesFullSet)
speciesHalfDiffQuar = speciesHalfSet.difference(speciesQuarSet)
speciesHalfInterQuarDiffFull = speciesHalfSet.intersection(speciesFullSet).difference(speciesFullSet)
speciesQuarDiffFull = speciesQuarSet.difference(speciesFullSet)
speciesQuarDiffHalf = speciesQuarSet.difference(speciesHalfSet)
speciesQuarInterFullDiffHalf = speciesQuarSet.intersection(speciesFullSet).difference(speciesHalfSet)


classAllIntersects = classFullSet.intersection(classHalfSet).intersection(classQuarSet)
classFullDiffHalf = classFullSet.difference(classHalfSet)
classFullDiffQuar = classFullSet.difference(classQuarSet)
classFullInterHalfDiffQuar = classFullSet.intersection(classHalfSet).difference(classQuarSet)
classHalfDiffFull = classHalfSet.difference(classFullSet)
classHalfDiffQuar = classHalfSet.difference(classQuarSet)
classHalfInterQuarDiffFull = classHalfSet.intersection(classFullSet).difference(classFullSet)
classQuarDiffFull = classQuarSet.difference(classFullSet)
classQuarDiffHalf = classQuarSet.difference(classHalfSet)
classQuarInterFullDiffHalf = classQuarSet.intersection(classFullSet).difference(classHalfSet)


genusAllIntersects = genusFullSet.intersection(genusHalfSet).intersection(genusQuarSet)
genusFullDiffHalf = genusFullSet.difference(genusHalfSet)
genusFullDiffQuar = genusFullSet.difference(genusQuarSet)
genusFullInterHalfDiffQuar = genusFullSet.intersection(genusHalfSet).difference(genusQuarSet)
genusHalfDiffFull = genusHalfSet.difference(genusFullSet)
genusHalfDiffQuar = genusHalfSet.difference(genusQuarSet)
genusHalfInterQuarDiffFull = genusHalfSet.intersection(genusFullSet).difference(genusFullSet)
genusQuarDiffFull = genusQuarSet.difference(genusFullSet)
genusQuarDiffHalf = genusQuarSet.difference(genusHalfSet)
genusQuarInterFullDiffHalf = genusQuarSet.intersection(genusFullSet).difference(genusHalfSet)


familyAllIntersects = familyFullSet.intersection(familyHalfSet).intersection(familyQuarSet)
familyFullDiffHalf = familyFullSet.difference(familyHalfSet)
familyFullDiffQuar = familyFullSet.difference(familyQuarSet)
familyFullInterHalfDiffQuar = familyFullSet.intersection(familyHalfSet).difference(familyQuarSet)
familyHalfDiffFull = familyHalfSet.difference(familyFullSet)
familyHalfDiffQuar = familyHalfSet.difference(familyQuarSet)
familyHalfInterQuarDiffFull = familyHalfSet.intersection(familyFullSet).difference(familyFullSet)
familyQuarDiffFull = familyQuarSet.difference(familyFullSet)
familyQuarDiffHalf = familyQuarSet.difference(familyHalfSet)
familyQuarInterFullDiffHalf = familyQuarSet.intersection(familyFullSet).difference(familyHalfSet)

orderAllIntersects = orderFullSet.intersection(orderHalfSet).intersection(orderQuarSet)
orderFullDiffHalf = orderFullSet.difference(orderHalfSet)
orderFullDiffQuar = orderFullSet.difference(orderQuarSet)
orderFullInterHalfDiffQuar = orderFullSet.intersection(orderHalfSet).difference(orderQuarSet)
orderHalfDiffFull = orderHalfSet.difference(orderFullSet)
orderHalfDiffQuar = orderHalfSet.difference(orderQuarSet)
orderHalfInterQuarDiffFull = orderHalfSet.intersection(orderFullSet).difference(orderFullSet)
orderQuarDiffFull = orderQuarSet.difference(orderFullSet)
orderQuarDiffHalf = orderQuarSet.difference(orderHalfSet)
orderQuarInterFullDiffHalf = orderQuarSet.intersection(orderFullSet).difference(orderHalfSet)

phylumAllIntersects = phylumFullSet.intersection(phylumHalfSet).intersection(phylumQuarSet)
phylumFullDiffHalf = phylumFullSet.difference(phylumHalfSet)
phylumFullDiffQuar = phylumFullSet.difference(phylumQuarSet)
phylumFullInterHalfDiffQuar = phylumFullSet.intersection(phylumHalfSet).difference(phylumQuarSet)
phylumHalfDiffFull = phylumHalfSet.difference(phylumFullSet)
phylumHalfDiffQuar = phylumHalfSet.difference(phylumQuarSet)
phylumHalfInterQuarDiffFull = phylumHalfSet.intersection(phylumFullSet).difference(phylumFullSet)
phylumQuarDiffFull = phylumQuarSet.difference(phylumFullSet)
phylumQuarDiffHalf = phylumQuarSet.difference(phylumHalfSet)
phylumQuarInterFullDiffHalf = phylumQuarSet.intersection(phylumFullSet).difference(phylumHalfSet)

PhylumSets = [PhylumAllIntersects,
PhylumFullDiffHalf,
PhylumFullDiffQuar,
PhylumFullInterHalfDiffQuar,
PhylumHalfDiffFull,
PhylumHalfDiffQuar,
PhylumHalfInterQuarDiffFull,
PhylumQuarDiffFull,
PhylumQuarDiffHalf,
PhylumQuarInterFullDiffHalf]

classSets = [classAllIntersects,
classFullDiffHalf,
classFullDiffQuar,
classFullInterHalfDiffQuar,
classHalfDiffFull,
classHalfDiffQuar,
classHalfInterQuarDiffFull,
classQuarDiffFull,
classQuarDiffHalf,
classQuarInterFullDiffHalf]

orderSets = [orderAllIntersects,
orderFullDiffHalf,
orderFullDiffQuar,
orderFullInterHalfDiffQuar,
orderHalfDiffFull,
orderHalfDiffQuar,
orderHalfInterQuarDiffFull,
orderQuarDiffFull,
orderQuarDiffHalf,
orderQuarInterFullDiffHalf]

familySets = [familyAllIntersects,
familyFullDiffHalf,
familyFullDiffQuar,
familyFullInterHalfDiffQuar,
familyHalfDiffFull,
familyHalfDiffQuar,
familyHalfInterQuarDiffFull,
familyQuarDiffFull,
familyQuarDiffHalf,
familyQuarInterFullDiffHalf]

genusSets = [genusAllIntersects,
genusFullDiffHalf,
genusFullDiffQuar,
genusFullInterHalfDiffQuar,
genusHalfDiffFull,
genusHalfDiffQuar,
genusHalfInterQuarDiffFull,
genusQuarDiffFull,
genusQuarDiffHalf,
genusQuarInterFullDiffHalf]


speciesSets = [speciesAllIntersects,
speciesFullDiffHalf,
speciesFullDiffQuar,
speciesFullInterHalfDiffQuar,
speciesHalfDiffFull,
speciesHalfDiffQuar,
speciesHalfInterQuarDiffFull,
speciesQuarDiffFull,
speciesQuarDiffHalf,
speciesQuarInterFullDiffHalf]

phylumSetLength = [len(p) for p in phylumSets]
classSetLengths = [len(c) for c in classSets]
orderSetLengths = [len(o) for o in orderSets]
familySetLengths = [len(f) for f in familySets]
genusSetLengths = [len(g) for g in genusSets]
speciesSetLengths = [len(s) for s in speciesSets]

phylumSetLists = [list(p) for p in phylumSets]
classSetListss = [list(c) for c in classSets]
orderSetListss = [list(o) for o in orderSets]
familySetListss = [list(f) for f in familySets]
genusSetListss = [list(g) for g in genusSets]
speciesSetListss = [list(s) for s in speciesSets]

setOperationKeys = ['All_intersections',
        'Full_vs_Half',
        'Full_vs_Quar',
        'Full_and_Half_vs_Quar',
        'Half_vs_Full',
        'Half_vs_Quar',
        'Half_and_Quar_vs_Full',
        'Quar_vs_Full',
        'Quar_vs_Half',
        'Quar_and_Full_vs_Half']


phylumSetOperationsTuple = zip(setOperationKeys, phylumSetLengths, phylumLists)
classSetOperationsTuple = zip(setOperationKeys, classSetLengths, classLists)
orderSetOperationsTuple = zip(setOperationKeys, orderSetLengths, orderLists)
familySetOperationsTuple = zip(setOperationKeys, familySetLengths, familyLists)
genusSetOperationsTuple = zip(setOperationKeys, genusSetLengths, genusLists)
speciesSetOperationsTuple = zip(setOperationKeys, speciesSetLengths, speciesLists)

phylumUniqueDF = pd.DataFrame.from_records(phylumSetOperationsTuple, columns=['Comparison', 'Size', 'Members'])
classUniqueDF = pd.DataFrame.from_records(classSetOperationsTuple, columns=['Comparison', 'Size', 'Members'])
orderUniqueDF = pd.DataFrame.from_records(orderSetOperationsTuple, columns=['Comparison', 'Size', 'Members'])
familyUniqueDF = pd.DataFrame.from_records(familySetOperationsTuple, columns=['Comparison', 'Size', 'Members'])
genusUniqueDF = pd.DataFrame.from_records(genusSetOperationsTuple, columns=['Comparison', 'Size', 'Members'])
speciesUniqueDF = pd.DataFrame.from_records(speciesSetOperationsTuple, columns=['Comparison', 'Size', 'Members'])

phylumUniqueDF.to_csv('phylumSetOperations.csv', index = False)
classUniqueDF.to_csv('classSetOperations.csv', index = False)
orderUniqueDF.to_csv('orderSetOperations.csv', index = False)
familyUniqueDF.to_csv('familySetOperations.csv', index = False)
genusUniqueDF.to_csv('genusSetOperations.csv', index = False)
speciesUniqueDF.to_csv('speciesSetOperations.csv', index = False)


