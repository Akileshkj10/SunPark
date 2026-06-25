import {
  faqItems,
  customerOutcomes,
  howItWorksPreview,
  installedSystem,
  moroccoContext,
  multiSiteExpansion,
  operatingPrinciples,
  operationsAfterLaunch,
  ppaExplainers,
  processSteps,
  processResponsibilities,
  publicMetrics,
  regulatorySupport,
  sectors,
  solutionModel,
  specialistSupport,
  sunparkResponsibilities,
  teamRoles,
} from "./site";

type SourceCheckedItem = {
  sourceNotes?: unknown[];
};

function hasSourceNotes(item: SourceCheckedItem) {
  return Array.isArray(item.sourceNotes) && item.sourceNotes.length > 0;
}

export function getMissingSourceNotes() {
  const groups = [
    { name: "publicMetrics", items: publicMetrics },
    { name: "howItWorksPreview", items: howItWorksPreview },
    { name: "moroccoContext", items: moroccoContext },
    { name: "solutionModel", items: solutionModel },
    { name: "installedSystem", items: installedSystem },
    { name: "customerOutcomes", items: customerOutcomes },
    { name: "sunparkResponsibilities", items: sunparkResponsibilities },
    { name: "multiSiteExpansion", items: multiSiteExpansion },
    { name: "processResponsibilities", items: processResponsibilities },
    { name: "regulatorySupport", items: regulatorySupport },
    { name: "operationsAfterLaunch", items: operationsAfterLaunch },
    { name: "operatingPrinciples", items: operatingPrinciples },
    { name: "specialistSupport", items: specialistSupport },
    { name: "ppaExplainers", items: ppaExplainers },
    { name: "sectors", items: sectors },
    { name: "processSteps", items: processSteps },
    { name: "teamRoles", items: teamRoles },
    { name: "faqItems", items: faqItems },
  ];

  return groups.flatMap((group) =>
    group.items
      .map((item, index) => ({ group: group.name, index, item }))
      .filter(({ item }) => !hasSourceNotes(item)),
  );
}

export function assertSourceNotes() {
  const missing = getMissingSourceNotes();

  if (missing.length > 0) {
    throw new Error(
      `Missing source notes: ${missing
        .map((entry) => `${entry.group}[${entry.index}]`)
        .join(", ")}`,
    );
  }
}
