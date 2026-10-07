// Hand-authored type fixture. It models the example schema, not a tenant-generated SDK.
import type { ObjectTypeDefinition, ObjectMetadata, PropertyDef, ActionDefinition, ActionMetadata, Osdk } from "@osdk/api";
export interface Todo extends ObjectTypeDefinition {
  type: "object";
  apiName: "Todo";
  __DefinitionMetadata?: ObjectMetadata & {
    type: "object";
    apiName: "Todo";
    primaryKeyApiName: "todoId";
    primaryKeyType: "string";
    links: {};
    properties: {
      todoId: PropertyDef<"string", "non-nullable">;
      title: PropertyDef<"string", "non-nullable">;
      isComplete: PropertyDef<"boolean", "non-nullable">;
      createdAt: PropertyDef<"timestamp", "non-nullable">;
    };
  };
}
export declare const Todo: Todo;
export declare const $ontologyRid: string;
export declare const completeTodo: ActionDefinition<{
  applyAction: (args: { todo: Osdk.Instance<Todo>; isComplete: boolean }) => Promise<unknown>;
}> & {
  apiName: "completeTodo";
  __DefinitionMetadata?: ActionMetadata & {
    signatures: { applyAction: (args: { todo: Osdk.Instance<Todo>; isComplete: boolean }) => Promise<unknown> };
    parameters: {
      todo: { type: { type: "object"; object: "Todo"; __OsdkTargetType?: Todo }; nullable: false; multiplicity: false };
      isComplete: { type: "boolean"; nullable: false; multiplicity: false };
    };
  };
};
